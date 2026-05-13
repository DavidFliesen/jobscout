import os
import json
import anthropic
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Cibola Job Scout Proxy')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/')
async def root():
    return {'status': 'online', 'service': 'Cibola Job Scout Proxy'}

@app.get('/health')
async def health():
    return {'status': 'online'}

@app.post('/scout')
async def scout(request: Request):
    try:
        body = await request.json()
        prompt = body.get('prompt', '')
        if not prompt:
            return JSONResponse({'error': 'No prompt provided'}, status_code=400)

        client = anthropic.Anthropic(api_key=os.environ['ANTHROPIC_API_KEY'])

        response = client.messages.create(
            model='claude-sonnet-4-20250514',
            max_tokens=4000,
            tools=[{'type': 'web_search_20250305', 'name': 'web_search'}],
            messages=[{'role': 'user', 'content': prompt}]
        )

        text_content = ''
        for block in response.content:
            if hasattr(block, 'text'):
                text_content += block.text

        clean = text_content.replace('```json', '').replace('```', '').strip()
        start = clean.find('{')
        end = clean.rfind('}')
        result = json.loads(clean[start:end+1])
        return JSONResponse(result)

    except json.JSONDecodeError as e:
        return JSONResponse({'error': 'JSON parse error', 'detail': str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse({'error': str(e)}, status_code=500)
