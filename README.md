# ChatGPT Bot with Streamlit

A simple, interactive chatbot built using OpenAI's GPT model and Streamlit. This application provides a clean, web-based interface for having educational conversations with ChatGPT.



## Prerequisites

Before running this application, run the requirements.txt file:


```bash
pip install -r requirements.txt
```



## Usage

To run the Streamlit application:

```bash
streamlit run source/main.py
```




## Configuration

The application uses a `config.json` file to store the OpenAI API key. Add your API key as follows:

```json
{
    "OPENAI_API_KEY": "your-api-key-here"
}
```

⚠️ Important: Never commit your actual API key to version control. Add `config.json` to your `.gitignore` file.


## Acknowledgments

- OpenAI for providing the GPT API
- Streamlit team for their amazing framework
- Contributors of the project

