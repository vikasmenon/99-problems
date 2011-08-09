def none_in_final_pos(pos_list, N):
  for x,y in zip(pos_list, [len(n) for n in N]):
     if x>=y:
        return False

  return True

def check_equals(pos_list, N):
  values = [y[x] for x,y in zip(pos_list, N)]
  val = values[0]
  results = map(lambda x: x == val, values[1:])
  if False in results:
     return False
  else:
     return True


def min_pos(values):
  if not values:
    # raise error accordingly
    return
  minimum = min(values)
  pos_list = []
  for i, val in enumerate(values):
      if val == minimum:
        pos_list.append(i)
  return pos_list



def get_intersection(N):
  result = []
  pos_list = [0] * len(N)
  while none_in_final_pos(pos_list, N):
     if check_equals(pos_list, N):
        result.append(N[0][pos_list[0]])
        pos_list = [pos + 1 for pos in pos_list]
     else:
        poses = min_pos([x[y] for x,y in zip(N, pos_list)])
        for pos in poses:
          pos_list[pos] += 1

  return result
