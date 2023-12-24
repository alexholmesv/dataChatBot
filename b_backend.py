#1. Load database using Langchain. Enter your database file in the argument for db.
from langchain.sql_database import SQLDatabase
db = SQLDatabase.from_uri("sqlite:///translations.db")

#2.Import APIs.
import a_env_vars
import os 
os.environ["OPEN_AI_API_KEY"] = a_env_vars.OPENAI_API_KEY

#3. Create the language model. Change the ChatGPT version here.
from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')

#4.Create the chain,
from langchain import SQLDatabaseChain
chain = SQLDatabaseChain(llm = llm, database = db, verbose = False)

#5. Question prompt format for personalized answer
formato = """
Dada una pregunta del usuario:
1. Crea una consulta de sqlite3
2. Revisa los resultados
3. Devuelve el dato
4. Si tienes que hacer alguna aclaración o devolver cualquier texto que sea siempre en español
#{question}
"""

#6. Query function
def makeQuery(user_input):
    query = formato.format(question = user_input)
    result = chain.run(query)
    return(result)

