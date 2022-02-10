import math

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

alphabet={'а':0,'б':0,'в':0,'г':0,'д':0,'е':0,'ё':0,'ж':0,'з':0,'и':0,'й':0,'к':0,'л':0,'м':0,'н':0,'о':0,'п':0,'р':0,'с':0,'т':0,'у':0,'ф':0,'х':0,'ц':0,'ч':0,'ш':0,'щ':0,'ъ':0,'ы':0,'ь':0,'э':0,'ю':0,'я':0}
symbols_frequency={'а':8.01,'б':1.59,'в':4.54,'г':1.70,'д':2.98,'е':8.54,'ё':0.04,'ж':0.94,'з':1.65,'и':7.35,'й':1.21,'к':3.49,'л':4.40,'м':3.21,'н':6.70,'о':10.97,'п':2.81,'р':4.73,'с':5.47,'т':6.26,'у':2.62,'ф':0.26,'х':0.97,'ц':0.48,'ч':1.44,'ш':0.73,'щ':0.36,'ъ':0.04,'ы':1.90,'ь':1.74,'э':0.32,'ю':0.64,'я':2.01}
symbol_sum=0
special_symbols=('.',',','-',' ','1','2','3','4','5','6','7','8','9','0','\n','?','!','–',':')
results={}
file_name = input('Input file path for truing to decrypt: ')
fp = open(file_name, 'r', encoding='utf-8')
for string in fp:
    for character in list(string):
        # print(character)
        symbol_sum+=1
        for symbol in alphabet:
            #print(symbol)
            if (character == symbol):
                #print(symbol)
                alphabet[symbol] += 1
    # for string in fp:
    #     print(string)
for item in alphabet:
    percentage=alphabet[item]/symbol_sum*100
    results[item]=round(percentage,2)
print('Full amount on symbols in text: ')
print(symbol_sum)
print('Amount particular symbold in text: ')    
print(alphabet)
print('Percentage of specific symbols in text: ')
print(results)
print('Symbols statistic: ')
print(symbols_frequency)
fp.close()

fp = open(file_name, 'r', encoding='utf-8')
fd = open('decrypted_text.txt', 'w', encoding='utf-8')

for string_item in fp:
    for character_item in list(string_item):
        if (character_item in special_symbols):
            fd.write(character_item)
        else:
            difference={}
            
            for s_item in symbols_frequency:
                difference[s_item]=round(abs(results[character_item.lower()]-symbols_frequency[s_item]),2)
            # print('Symbol for replacement: ')
            # print(get_key(difference,min(difference.values())))
            # print(difference)
            fd.write(get_key(difference,min(difference.values())))
            # # print(results[symbol_item])
            # # print(symbols_frequency[symbol_item])
            # if (math.isclose(results[symbol_item],symbols_frequency[symbol_item])):
            #     # print(results[symbol])
            #     # print(symbols_frequency[symbol])
            #     fd.write(symbols_frequency[symbol_item])
fd.close()
fp.close()