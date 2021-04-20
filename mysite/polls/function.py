from mysite.settings import BASE_DIR
import pandas as pd
import datetime

def create_member(csv_pass):
    #df = pd.read_csv( BASE_DIR + '/media/output/huga.csv', header=0)# パス指定の問題は後で
    df = pd.DataFrame(
            [
                ['2021-04-01T12:00:00','2021-04-01T12:10:00','山口','議事録開始！！！！'],
                ['2021-04-01T12:20:01','2021-04-01T12:20:30','山口','どんなファイルが読み込まれた？'],
                ['2021-04-01T12:30:00','2021-04-01T12:40:00','山田','output_file_pass_name'],
                ['2021-04-01T12:50:00','2021-04-01T12:45:00','山田','Yes.'],
                ['2021-04-01T12:50:00','2021-04-01T12:50:40','山目','This is a long long long long long long long long long long long long sentence.  How is this shown?  Good or Very Good?'],
                ['2021-04-01T13:00:00','2021-04-01T13:30:00','山廿','アパー']
            ],
            columns = ['start time','end time','member','speech']
        )


    start_time = datetime.datetime.strptime(df['start time'][0], '%Y-%m-%dT%H:%M:%S')
    end_time = datetime.datetime.strptime(max(list(df['end time'])), '%Y-%m-%dT%H:%M:%S')
    meeting_time = (end_time - start_time).total_seconds()

    member_list_name = df['member'].unique()

    list_member = [{ 
        'name' : member_list_name[i],
        'class_name' : 'member' + str(i),
        'speech_info' : [{
            'speech' : j[1]['speech'],
            'class_name' : 'member' + str(i) + '_speech_element' + str(k),
            'position' : round((datetime.datetime.strptime(j[1]['start time'], '%Y-%m-%dT%H:%M:%S') - start_time).total_seconds() *1000 / meeting_time ),
            'width' : round((datetime.datetime.strptime(j[1]['end time'], '%Y-%m-%dT%H:%M:%S') - datetime.datetime.strptime(j[1]['start time'], '%Y-%m-%dT%H:%M:%S')).total_seconds() * 1000 / meeting_time )
        } for j, k in zip(df[df['member'] == member_list_name[i]].reset_index(drop = True).iterrows(), range(len(df[df['member'] == member_list_name[i]])))]
    } for i in range(len(member_list_name))]

    return list_member