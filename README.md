# LangChain Framework Exploration

This project is an attempt to explore and experiment with the LangChain framework.
I am taking reference from the following video:  
YouTube Video: [LangChain Video](https://www.youtube.com/watch?v=nAmC7SoVLd8)

## How to Run This Code

To start the application, use the following command:
```sh
streamlit run main.py
```

### Creating a Secret Key File
Create a file named `secret_key.py` in the same directory as `main.py` and add the following content:
```python
openai_key = "<Your Open AI API key>"
```

---

## Project Initialization Using Conda

I am using the Conda framework for project setup.

### Steps to Set Up the Environment

1. Create a new Conda environment:
   ```sh
   conda create --prefix ./env python=3.10
   ```
2. Activate the environment:
   ```sh
   conda activate ./env
   ```
3. Verify Python installation:
   ```sh
   python --version
   ```
4. List installed packages:
   ```sh
   conda list
   ```

---

## Required Packages

The necessary dependencies are listed in `requirements.txt`:
```txt
openai
langchain
streamlit
langchain-community
```

### How to Install Dependencies
Run the following command to install all required packages:
```sh
pip install -r requirements.txt
```

---

## Summary
- This project is for learning and experimenting with the LangChain framework.
- The environment is managed using Conda.
- Dependencies are installed via pip.

Happy coding! 🚀
