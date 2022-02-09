from math import ceil

def get_options_for_next_step (bricks):
    if bricks < 3:
        return 0
    num_of_options = bricks - (ceil(((8*bricks+1)**(0.5)-1)/2))
    #print('num of->', num_of_options)
    #print ('opt list->',[option for option in range(bricks-num_of_options, bricks)], 'for ', bricks, ' bricks')
    return [option for option in range(bricks-num_of_options, bricks)]

def accumulate_options (bricks):
    acc = 0
    while bricks >= 3:
        options = get_options_for_next_step(bricks)
        if len(options) == 0:
            break
        print('op->',len(options))
        acc += len(options)
        bricks = bricks - options[0]
        print('acc',acc)

    return acc

def accumulate_options_a (bricks):
    acc = 0
    options = get_options_for_next_step(bricks)
    acc = len(options)
    acc += recu(options, acc)
    return acc
   
def recu (options, acc):
    if not options:
        return acc
    for i in range (len(options)):
        #print(options, options[i])
        for j in range (len(options[i:len(options)])):
            print(options, options[j])
            acc += sum(get_options_for_next_step(options[j])) 
        #print ('acc',acc, options)

    options = options[1::]
    return recu (options, acc)

def p(n, d=0):
  if n:
    return sum(p(n-k, n-2*k+1) for k in range(1, n-d+1))
  else:
    return 1

def Q(n):
    # Represent polynomial as a list of coefficients from x^0 to x^n.
    # G_0 = 1
    G = [int(g_pow == 0) for g_pow in range(n + 1)]
    print (' G',G, 'total: ' ,n)
    for k in range(1, n):
        # G_k = G_{k-1} * (1 + x^k)
        # This is equivalent to adding G shifted to the right by k to G
        # Ignore powers greater than n since we don't need them.
        #G = [G[g_pow] if g_pow - k < 0 else G[g_pow] + G[g_pow - k] for g_pow in range(n + 1)]
        rep = [i for i in G]
        for g_pow in range (n+1):
            #print('--',G[g_pow])
            if g_pow -k < 0:
                rep[g_pow] = G[g_pow]
                #print ('g_pow:', g_pow, ' G[g_pow]:', G[g_pow])
            else:
                rep[g_pow] = G[g_pow] + G[g_pow - k]
                print (rep, 'g_pow', g_pow, 'G[g_pow]', G[g_pow] , 'G[g_pow - k]', G[g_pow - k])
        print ('2G', rep)
        G = [i for i in rep]
    return G[n]

print ('sol',Q(15))

