# Text_Summarizer_App
An abstractive text summarization web application that takes English instructions-based text and delivers a summary in command format.

*Please be advised that the model is not fully fine-tuned. Hence the tool might produce inaccurate results.* 

To run the application:
1. Create and switch to a virtual environment (python >= 3.3.0)
2. Install requirements
`pip install -r requirements.txt`
3. Clone the repository
`git clone https://github.com/RajithaMuthukrishnan/Text_Summarizer_App.git`
4. Navigate to the `frontend` folder
5. Execute `python manage.py runserver`

The code for model training can be found in the `bilingual_bart.ipynb` notebook in the `model` folder

![alt text](https://github.com/RajithaMuthukrishnan/Text_Summarizer_App/blob/main/Homepage.png?raw=true)
