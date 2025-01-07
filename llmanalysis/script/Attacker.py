from typing import List, Dict
    

class Attacker:

    def prompt_multiple_choice_feature(attack_features:List[str], code:str)->str:

        question_template="""Given the following smart contract code, answer the questions below and organize the result in a json format like {"""
    
        for index, feature in enumerate(attack_features):
            question_template += f'"{index+1}": "Yes" or "No"'
            if index != len(attack_features)-1:
                question_template += ', '

        question_template += f'}}.\n'

        for index, feature in enumerate(attack_features):
            question_template += f'"{index+1}": Does it "{feature}"?\n'
    
        question_template += f'\n{code}'
    
        return question_template


    def prompt_single_choice_model(attacker_model:str,code:str)->str:

        question_template = f"""Does the following smart contract code {attacker_model}? Answer only "Yes" or "No".

        {code}
        """
        return question_template
