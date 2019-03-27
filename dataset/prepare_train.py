import pickle
def process_csv(filename='train_rand.pkl'): 
  entries = []
  with open('random.log') as f:
    lines = f.readlines()

    for line in lines:
      data = line.split('],') 
      obs = data[0].replace('[','').split(',')
      obs = list(map(lambda x: int(x), obs))
            
      tmp = data[1].split(',') 
      act = tmp[0]
      rew = tmp[1]
      
      entries.append((obs, act, rew))
  
  output = open(filename, 'wb')
  pickle.dump(entries, output)
  output.close()

def load_data(filename='train_rand.pkl'):
  pkl_file = open(filename, 'rb')
  entries = pickle.load(pkl_file)
  obs, act, rew = entries[0]
  pkl_file.close()
  print("{} {} {}".format(obs, act, rew))


process_csv()
load_data()
  
      