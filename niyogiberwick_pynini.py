"""
Based on Niyogi & Berwick 1997. 

"""
    #set of grammars G
    
    #g in G defines some language L(g) in sigma star 
    #sentences of sigmastar from a certain g presented to individual learner
    #probability[algorithm(samples) - g]
    
    #update rule
    #P(word) = sum P(w) * P

import pynini 
import functools 
import math

A = functools.partial(pynini.acceptor, token_type="utf8")
T = functools.partial(pynini.transducer, input_token_type="utf8", output_token_type="utf8")
e = pynini.epsilon_machine()

#build markov chains a la N/B 
#states:
#   Proto-West-Slavic
#   Czech (vowel length retained)
#   Polish 1 (raising as a phonological change
#   Polish 2 (raising as a morphological process)
#   Polish 3 (lexicalized raising)
#   Silesian ? 

class Speaker():
    """
    A single speaker in a population. 
    """
    def __init__(self, pre = False, ind):
        self.language = language(pre, ind)
        self.community = True
        
    def language(self, pre, ind=-1):
        """
        Set language tag for current speaker.
        """
        
        if pre:
            #set default based on individual value
            n = 100
            if ind in range(95):
                return "PWS"
            elif ind in range(94, 97)
                return "CZECH"
            elif ind== 97:
                return "P_PHON"
            elif ind==98:
                return "P_MORPH"
            elif ind==99:
                return "P_LEX"
        else:
            return learn(pre)
            pass
        return True
        
    def learn(self, pre, mode="POP"):
        """
        Based on sampling method (cohort or individual), picks a sampling method and determines the language state for the current speaker.
        """
                
        #how to 'learn' from these samples ? how to define transition matrix & weights? - see gorman book
        
        
        pass
        
    def sampling(self, pre):
        """
        Individual-level sampling - probability of picking a sample from members of the same community can be increased, and probability of picking a sample for another community can be penalized. 
        """
        pass

class Population():
    
    """
    Establish population as a collection of speakers per generation.
    """
    
    def __init__(self, pre = False, n = 100):
        """
        Create new generation of speakers. Standard set to 100 speakers, but can be adjusted for larger/smaller populations.
        
        generation: counts generation *from present*, not current number of generation.
        pre: precursor generation, create a linked list of generation
        n: number of speakers per generation
        """
        self.generation = 1
        self.cycle(1)
        
        if not pre: 
            #If this is the first generation, all Speakers must be made from original data
            pop = []
            for x in range(n):
                pop.append(Speaker(x))
            
            self.pop = pop
        else:
            #else, speakers must learn from previous generation
            for x in range(len(self.pop)):
                self.pop[x].language(pre=pre)

    
    def cycle(self, mode="LOG"):
        """
        Updates generational decay, known as 'stagger'. Default is logarithmic decay, but I include exponential to play around with.
        """
        self.generation++
        if mode == "LOG":
            #logarithmic decay
            self.stagger = math.log(1 / self.generation)
            pass
        elif mode == "EXP":
            #exponential decay
            self.stagger = 10 ** (self.generation * -1)
            
    def sample(self, n = 25):
        """
        Population-level sampling.
        """
        pass 
        
    def divide(self, comms: list):
        """
        When communities allowed, divides generation into subsets of communities to prepare for individual-level sampling.
        """
        pass

    
    
#--------------------------    

def learn(family):
    """
    
    """
    if family:
        n = Population(pre=family)
        return n
    else:
        family = Population()
        return family

if __name__ == "__main__":
    """
    Initializing program will create one generation. Every subsequent 'learn' iteration will add a new generation. 
    """
    family = learn(False)
    

    
    
    

