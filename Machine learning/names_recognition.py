import pandas as pd
import re

#assb
def load():
    ru_user_names = pd.read_excel(r'C:\Users\user\Google Drive\סאיקאן\Projects\Abbvie\data\profiles_names.xlsx')['profile name'].tolist()
    profiles_names = pd.read_excel(r'C:\Users\user\Google Drive\סאיקאן\Projects\Abbvie\data\profiles_names.xlsx')['profile name'].tolist()
    return ru_user_names, profiles_names

def classsifier(ru_user_names, profiles_names):
    profiles_names_classification = []
    ru_user_names_set = set(ru_user_names)
    for i in range(len(profiles_names)):
        if(has_cyrillic(profiles_names[i])):
            profiles_names_classification.append(1)
        else:
            if(profiles_names[i] in ru_user_names_set):
                profiles_names_classification.append(1)
            else:
                profiles_names_classification.append(0)

    return profiles_names_classification


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


if __name__ == '__main__':
    ru_user_names, profiles_names = load()
    profiles_names_classification = classsifier(ru_user_names, profiles_names)
    pd.DataFrame(profiles_names).to_excel('ru profiles_names results.xlsx')
    print(has_cyrillic('Анна Генриховна'))
    for i in range(len(ru_user_names)):
        try:
            print(ru_user_names[i].split()[1])
        except:
            print('problem')
