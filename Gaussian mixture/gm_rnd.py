from scipy.stats import uniform

def gm_rnd(mu, sigma, p):
    resultat = 0.0
    if len(mu) != len(p):
        print('Erreur de dimension sur la moyenne')
    elif len(sigma) != len(p):
            print('Erreur de dimension sur la variance')
    else:
        u = uniform.rvs(loc = 0.0, scale = 1.0, size = 1)
        if u < p[0]:
            resultat = sigma[0] * norm.rvs(loc = 0.0, scale = 1.0, size = 1) + mu[0]
        for i in range(1, len(p)):
            if (u > np.sum(p[0:i])) and (u<= np.sum(p[0:i+1])):
                resultat = sigma[i] * norm.rvs(loc = 0.0, scale = 1.0, size = 1) + mu[i]
    return resultat