import random

BIGRAM = ['th','en','ng','he','ed','of','in','to','al','er','it','de','an','ou','se','re','ea','le','nd','hi','sa','at','is','si','on','or','ar','nt','ti','ve','ha','as','ra','es','te','ld','st','et','ur']
TRIGRA = ['the','ing','tha','ere','eth','hat','for','sth','est','his','hes','ers','oth','dth','tth','rea','wit','are','res','tin','rth','sof','you','sto','edt','eve','ast','din','con','sta','nce','ght','man','not','out','esa','she','ngt','eri','ndt','att','ave','hin','ive','ine','hec','rin','nde','han','igh','ent','que','des','est','eme','sde','lle','tre','ant','our','del','nte','eur','tio','ien','ont','sse','ite','sle','con','ess','nde','tes','equ','ais','ete','che','ell','rle','tle','pre','uel','nes','ill','ise','eet','sen','ous','eso','epa','tou','dec','onn','era','ntd','urs','nta','etr','rai','ain']
CONSAN = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
VOWELS = ['a','e','i','o','u','y']
NUMBER = [0,1,2,3,4,5,6,7,8,9]

# Ensure random number doesnt return as zero
def rndnum():    
    end = 0
    while end == 0:
        end = ((random.choice(NUMBER)) * round(random.random() / 2 * 1000))
    return str(end)

# Generate predfined word using BIGRAM (Change to TRIGRAM for longer word)
def wrdgen():
    wrd = random.sample(CONSAN,1)
    wrd.insert(1,random.choice(VOWELS))
    wrd.append(random.choice(BIGRAM))
    wrd.append(random.choice(VOWELS))
    wrd.append(random.choice(CONSAN))
    wrd.append(rndnum())
    return "".join(wrd)