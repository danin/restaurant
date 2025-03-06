LangChain Framework Exploration

This is an attempt to try the LangChain framework.
I am taking reference from the following video:
YouTube Video: https://www.youtube.com/watch?v=nAmC7SoVLd8

#How to run  this code:
streamlit run main.py

#create a file "secret_key.py" on the same level as main.py
Add following content:
openai_key = "<Your Open AI API key>" 



---

Project Initialization Using Conda

I am using the Conda framework for project setup.

Steps to Set Up the Environment:

1. Create a new Conda environment:
   conda create --prefix ./env python=3.10

2. Activate the environment:
   conda activate ./env

3. Verify Python installation:
   python --version

4. List installed packages:
   conda list

---

Required Packages

The necessary dependencies are listed in requirements.txt:

openai
langchain
streamlit
langchain-community

How to Install Dependencies:
Run the following command to install all required packages:

pip install -r requirements.txt

---

Summary
- This project is for learning and experimenting with the LangChain framework.
- The environment is managed using Conda.
- Dependencies are installed via pip.

Happy coding!