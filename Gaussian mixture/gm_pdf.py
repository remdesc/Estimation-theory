from scipy.stats import norm

def gm_pdf(x, mu, sigma, p):
    resultat = 0
    if len(mu) != len(p):
        print('Erreur de dimension sur la moyenne')
    elif len(sigma) != len(p):
            print('Erreur de dimension sur la variance')
    else:
        for i in range(0, len(p)):
            resultat = resultat + p[i] * norm.pdf(x = x, loc = mu[i], scale = sigma[i])
    return resultat

