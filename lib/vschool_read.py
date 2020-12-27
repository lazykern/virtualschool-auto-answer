import pandas as pd
import os

data = pd.read_csv('/home/lloli/Documents/GitHub/Sorn/all.csv')
class read:
    def __init__(self, file):
            self.file = file 
            
    def to_qa(self):
            lines_new = []

            with open(self.file,'r') as f:
                lines = [x.replace('\ufeff', '') for x in f.readlines()]

            for element in lines:
                lines_new.append(element.strip())

            quiz = []
            answer = []

            for string in lines_new:
                if 'ข้อสอบ' in string:
                    if 'ถูก' in lines_new[lines_new.index(string)+3]:
                        quiz.append(string.split(' ')[-1].replace('ข้อสอบ','').replace('\n', ''))
                        answer.append(lines_new[lines_new.index(string)+3].replace('คำตอบข้อที่ถูก', '').replace(' ', '').replace('\n', ''))
            
            return quiz, answer
        
    def to_df(self):
        lines_new = []

        with open(self.file,'r') as f:
            lines = [x.replace('\ufeff', '') for x in f.readlines()]

        for element in lines:
            lines_new.append(element.strip())

        quiz = []
        answer = []

        for string in lines_new:
            if 'ข้อสอบ' in string:
                if 'ถูก' in lines_new[lines_new.index(string)+3]:
                    quiz.append(string.split(' ')[-1].replace('ข้อสอบ','').replace('\n', ''))
                    answer.append(lines_new[lines_new.index(string)+3].replace('คำตอบข้อที่ถูก', '').replace(' ', '').replace('\n', ''))

        df = pd.DataFrame(
            {'id': quiz,
            'ans_TH': answer
            })
        di = {
            'ก': 1,
            'ข': 2,
            'ค' : 3,
            'ง' : 4,
            'จ' : 5
            }
        df['ans'] = df['ans_TH'].replace(di)
                
        delet = []

        for v in df['id'].values:
            if v.count('-') > 3: 
                delet.append(df[df['id'] == str(v)].index[0])

        for i in list(df[df['ans'] == ''].index) :
            delet.append(i)

        for i in list(df[(df['id'].duplicated()) & (df['ans'].duplicated() == False)].index) :
            delet.append(i)

        df = df.drop(delet)
        df = df.drop_duplicates()
        

        return df.reset_index().drop(columns='index')
    
    def to_csv(self,csv_path):
        lines_new = []

        with open(self.file,'r') as f:
            lines = [x.replace('\ufeff', '') for x in f.readlines()]

        for element2 in lines:
            lines_new.append(element2.strip())

        quiz = []
        answer = []

        quiz = []
        answer = []

        for string in lines_new:
            if 'ข้อสอบ' in string:
                if 'ถูก' in lines_new[lines_new.index(string)+3]:
                    quiz.append(string.split(' ')[-1].replace('ข้อสอบ','').replace('\n', ''))
                    answer.append(lines_new[lines_new.index(string)+3].replace('คำตอบข้อที่ถูก', '').replace(' ', '').replace('\n', ''))

        df = pd.DataFrame(
            {'id': quiz,
            'ans_TH': answer
            })
        di = {
            'ก': 1,
            'ข': 2,
            'ค' : 3,
            'ง' : 4,
            'จ' : 5
            }
        df['ans'] = df['ans_TH'].replace(di)
                
        delet = []

        for v in df['id'].values:
            if v.count('-') > 3: 
                delet.append(df[df['id'] == str(v)].index[0])

        for i in list(df[df['ans'] == ''].index) :
            delet.append(i)

        for i in list(df[(df['id'].duplicated()) & (df['ans'].duplicated() == False)].index) :
            delet.append(i)
            

        df = df.drop(delet)
        df = df.drop_duplicates()
        
        df.reset_index().drop(columns='index').to_csv(csv_path)
        
    
    def to_csv_2line(self,csv_path):
        lines_new = []

        with open(self.file,'r') as f:
            lines = [x.replace('\ufeff', '') for x in f.readlines()]

        for element2 in lines:
            lines_new.append(element2.strip())

        quiz = []
        answer = []

        quiz = []
        answer = []

        for string in lines_new:
            if 'ข้อสอบ' in string:
                if 'ถูก' in lines_new[lines_new.index(string)+2]:
                    quiz.append(string.split(' ')[-1].replace('ข้อสอบ','').replace('\n', ''))
                    answer.append(lines_new[lines_new.index(string)+2].replace('คำตอบข้อที่ถูก', '').replace(' ', '').replace('\n', ''))

        df = pd.DataFrame(
            {'id': quiz,
            'ans_TH': answer
            })
        di = {
            'ก': 1,
            'ข': 2,
            'ค' : 3,
            'ง' : 4,
            'จ' : 5
            }
        df['ans'] = df['ans_TH'].replace(di)
                
        delet = []

        for v in df['id'].values:
            if v.count('-') > 3: 
                delet.append(df[df['id'] == str(v)].index[0])

        for i in list(df[df['ans'] == ''].index) :
            delet.append(i)

        for i in list(df[(df['id'].duplicated()) & (df['ans'].duplicated() == False)].index) :
            delet.append(i)
            

        df = df.drop(delet)
        df = df.drop_duplicates()
        
        df.reset_index().drop(columns='index').to_csv(csv_path)
    
        
        
def to_csv(file_path,csv_path):
    f = read(file_path)
    f.to_csv(csv_path)
    file_name = file_path.split('/')[-1]
    csv_name = csv_path.split('/')[-1]
    print( file_name, ' to', csv_name)

def to_csv_2n(file_path,csv_path):
    f = read(file_path)
    f.to_csv_2line(csv_path)
    file_name = file_path.split('/')[-1]
    csv_name = csv_path.split('/')[-1]
    print( file_name, ' to', csv_name)

    
def concat(input_dir,output_path):
    all_df = pd.DataFrame()

    for csv in os.listdir(input_dir):
        df = pd.read_csv(os.path.join(input_dir,csv))
        all_df = pd.concat([all_df,df])
        
    all_df = all_df.sort_values('id').drop_duplicates().reset_index().drop(columns='index')
    
    all_df.to_csv(output_path,columns=['id','ans_TH','ans'],index=False)

def answer(ID):
    data = pd.read_csv('/home/lloli/Documents/GitHub/Sorn/all.csv')
    data = data.drop(data[data['id'] == data['ans']].index) 
    data2 = pd.DataFrame()
    data2['id'] = data['id']
    data2['ans'] = data['ans']
    data2.to_csv('/home/lloli/Documents/GitHub/Sorn/all.csv',index=False)
    data = data2

    d  = data[data['id'] == ID.split(' ')[-1]].values
    ID_CLEAN = ID.split(' ')[-1]
    if not d.shape[0] == 0:
        ans = data[data['id'] == ID_CLEAN]['ans'].values[0]
        return int(ans)
    else:
        return None
        
