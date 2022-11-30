#check datatypes of certain columns
cols = ["MKOPEN", "MKCLOSE", "MKEMHOPEN", "MKEMHCLOSE", "MKOPENYEST", "MKCLOSEYEST", "MKOPENTOM", "MKCLOSETOM", "EPOPEN", "EPCLOSE", "EPEMHOPEN",
"EPEMHCLOSE", "EPOPENYEST", "EPCLOSEYEST", "EPOPENTOM", "EPCLOSETOM", "AKOPEN", "AKCLOSE", "AKEMHOPEN", "AKEMHCLOSE", "AKOPENYEST", "AKCLOSEYEST",
"AKOPENTOM", "AKCLOSETOM", "MKPRDDT1", "MKPRDDT2", "MKPRDNT1", "MKPRDNT2", "MKFIRET1", "MKFIRET2", "EPFIRET1", "EPFIRET2", "AKSHWNT1", "AKSHWNT2"]
types = {}
for col in cols:
    dist = []
    for row in range(len(metadata[col])):
        dist.append(str(type(metadata[col][row])))
    types[col] = list(set(dist))

col_float =  [col for col, dt in types.items() if "<class 'float'>" in dt]
col_float

for row in metadata["MKPRDNT1"]:
    if str(type(row)) == "<class 'float'>":
        print(row)
#nan is treated as float???

#standardization?????
# lm = LinearRegression()
# lm.fit(X_train, y_train)
# y_pred = lm.predict(X_test)

# print("RMSE: " + str(round(sqrt(mean_squared_error(y, y_pred)), 2)))
# print("R_squared: " + str(round(r2_score(y, y_pred), 2)))


x[col] = x[col].apply(lambda h: h[:2] if h[0] != 0 else h[:1]).astype(int).astype("Int8")
            for time in dataframe[col]:
                    if len(time)==4:
                        time = '0'+ time
                    if len(time)==5 and time > '24:00':
                        hour = int(time[:2])-24
                        minute = time[-2:]
                        time = str(hour) + ':' + minute
                    if time 
                #convert string to datetime 
                    time = pd.to_datetime(time, format="%H:%M")
                #convert datetime to float
                    time = time.hour + (time.minute/60)