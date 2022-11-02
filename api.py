from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def json_response():
    slackUsername = 'Yelosolutions'  
    bio = 'get the skills'

    return {'slackUsername': slackUsername, "backend": bool('YES'), "age": int('32'), "bio": bio}