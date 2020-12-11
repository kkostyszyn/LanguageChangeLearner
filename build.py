import pynini 
import functools
import pywrapfst as pywrap

A = functools.partial(pynini.acceptor, token_type="utf8")
T = functools.partial(pynini.transducer, input_token_type="utf8", output_token_type="utf8")
e = pynini.epsilon_machine()

def alpha_gen(alph, e):
    """
    Define the states used.
    """
    zero = (e - e).optimize()
    sigma = zero
    for x in list(alph):
        sigma = A(x) | sigma
    sigma = pynini.closure(sigma)
    return sigma.optimize()
    

    

if __name__ == "__main__":
    
    
