import matplotlib.pyplot as plt

def plotter(tuple_data):
	t = tuple_data
	if len(t)== 1:
	    if 'Literacy' in t[0][1]:
	        labels = ['Literate','Illiterate']
	        pct = t[0][3][:-1]
	        pct = int(pct)
	        values = [pct,100-pct]
	        plt.pie(values, labels = labels, autopct = '%1.1f', explode = [0.05,0])
	        plt.title(t[0][1]+" "+t[0][2]+" "+t[0][4])
	        plt.axis('equal')
	        #plt.show()
	        plt.savefig('Image.png')
	    else:
	        print(t)
	        labels = [t[0][2]+" "+t[0][4]]
	        if "%" in t[0][3]:
	            values = [float(t[0][3][:-1])]
	        else:
	            values = [get_number(t[0][3])]
	        plt.bar(labels, values, width = 0.01)
	        plt.title(t[0][1])
	        #plt.show()
	        plt.savefig('Image.png')

	#Multiple values plot bar graph
	else:
	    if '%' not in t[0][3]:
	        labels = []
	        values = []
	        for i in t:
	            labels.append(i[2]+' '+i[4])
	            try:
	                values.append(w2n.word_to_num(i[3]))
	            except:
	                values.append(float(i[3]))
	        plt.bar(labels, values, align = 'center')
	        plt.ylabel(t[0][1])
	        plt.title(t[0][0])
	    else:
	        labels = []
	        values = []
	        for i in t:
	            labels.append(i[2]+' '+i[4])
	            values.append(w2n.word_to_num((i[3][:-1])))
	        plt.bar(labels, values, align = 'center')
	        plt.ylabel(t[0][1])
	        plt.title(t[0][0])
	    plt.savefig('Image.png')
