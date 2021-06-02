def proc(temp):
        tsex = ['Female','Male']
        tfbs = ['Less than 120mg/dl','Greater than 120mg/dl']
        trestecg = ['Normal','ST-T wave abnormality','Left vascular hyperthropy']
        texang = ['Yes','No']
        tslope = ['','Upsloping','Flat','DownSloping']
        tcp = ['Typical Angin','Atypical Angina','Non-Anginal pain','Asymptomatic']
        temp['sex'] = tsex[int(temp['sex'])]
        temp['fbs'] = tfbs[int(temp['fbs'])]
        temp['restecg'] = trestecg[int(temp['restecg'])]
        temp['exang'] = texang[int(temp['exang'])]
        temp['slope'] = tslope[int(temp['slope'])]
        temp['cp'] = tcp[int(temp['cp'])]
        return temp
        