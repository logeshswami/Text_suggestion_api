import random

#FUNCTION TO GENERATE WORDS USING MARKOV CHAIN PASSED AS ARGUMENT
def generate( model,n = 2, start=None, max=1):
  try:
      if start is None :
        return " "
      output = list(start)
      for i in range(max):
        start = tuple(output[-n:])
        next = random.choice(model[start])
        if next is None:
          break
        else:
          output.append(next)
      return " ".join(output[n:])

  except(KeyError):
    return " ".join(start)