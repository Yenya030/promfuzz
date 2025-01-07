from typing import List, Dict



class Invariant:

    def prompt_variable_and_statement_analysis(questions:List[str], code:str) -> str:


        question_template="""Please answer the questions below and organize the result in a json format like {"""
    
        for index, question in enumerate(questions):
            question_template += f'"{index+1}": "Your Answer"'
            if index != len(questions)-1:
                question_template += ', '

        question_template += f'}}.\n'

        for index, question in enumerate(questions):
            question_template += f'"{index+1}": "{question}"\n'
    
        question_template += f'\n{code}\n'
    
        return question_template
    

