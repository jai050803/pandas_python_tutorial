import pandas as pd

df = pd.DataFrame({
  'name' : ['aman','rizwan','raghav','sunny'],
  'rollno' : [1,2,3,4],
  'marks' : [98,99,100,100]
})

print(df.to_string())

