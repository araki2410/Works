#!/usr/bin/python
# -*- coding:utf-8 -*-

import json
import sys
import commands  #typeset for texfile

# argvs = sys.argv
# argc = len(argvs)

filedir = "./File/" #in an image and for output file 
openfile = "./entry.json" # input file name
outputname = "output"
outputfile = outputname + ".tex"
with open(openfile,'r') as f:
    textdata = json.loads(f.read(), 'utf-8')
data = open(openfile,'r')
textdata = json.load(data)
data.close
uname = textdata["usename"].encode('utf-8')

texfile = open("templateentry.tex","r")
textext = texfile.read()
texfile.close


for i in textdata["data"]:
    print i["question"].encode('utf-8')
    print i["answer"].encode('utf-8')
#print textdata["data"][0]["answer"]

#quit()
textext += '''
\\begin{table}[t]
 \scalebox{1.1}[1.2]{
  \\begin{tabular}{|l|c|c|c|c|c|}
   \cline{1-5}
   ふりがな & \multicolumn{4}{|p{26em}|}{ふりがなhogehoge}  & \multicolumn{1}{|c}{\multirow{5}{40mm}{
\\begin{minipage}{30mm}
    \centering
    \scalebox{0.4}{\includegraphics{./File/crow.eps}}
   \end{minipage}}} \\\\ \cline{1-5} 
   氏名 & \multicolumn{4}{|l|}{}\\\\

    & \multicolumn{4}{|l|}{\Large %s}\\\\ \cline{1-5}

   生年月日 &  \multicolumn{3}{|c|}{1918-12-8} & 男 \\\\ \cline{1-5}

   電話番号 & \multicolumn{4}{|l|}{042(443)5102}  \\\\ \cline{1-5}
   E-mail & \multicolumn{4}{|l|}{hogehogehoge@cs.euc.ac.jp}  \\\\ \hline

   ふりがな & \multicolumn{4}{|l|}{ふりがなhogehoge juusho 1-5-1} & 電話 \\\\ \cline{1-5}

    郵便番号〒 & \multicolumn{4}{|l|}{182-8585} & \multirow{2}{*}{042(443)5102}\\\\ 
     & \multicolumn{4}{l|}{kanji juusho} & \\\\ \hline

   ふりがな & \multicolumn{4}{|l|}{} & 電話 \\\\ \cline{1-5}
   連落先〒 & \multicolumn{4}{|l|}{(現住所以外に連絡を希望する場合のみ記入)} & \multirow{2}{*}{042(443)5102} \\\\
   & \multicolumn{4}{|l|}{} & \\\\
   \hline
  \end{tabular}
}

\end{table}


''' % uname

textext += "\section{%s}" %  textdata["data"][1]["answer"].encode('utf-8')
textext += "\n\end{document}"

output = open(filedir+outputfile,"w")
output.write(textext)

dname = filedir + outputname

mkdvi = "platex " + filedir + outputfile
mkpdf = "dvipdfmx " + outputname + ".dvi" + " -o " +  dname + ".pdf"
rmfile = "rm -f " + outputname + ".aux " + outputname + ".log " + outputname + ".dvi"

# mkdvi = commands.getoutput("platex " + filedir + outputfile)
# mkpdf = commands.getoutput("dvipdfmx " + outputname + ".dvi" + " -o " +  dname + ".pdf")
# rmfile = commands.getoutput("rm -f " + outputname + ".aux " + outputname + ".log " + outputname + ".dvi")
print mkdvi
print mkpdf
print rmfile
commands.getoutput(mkdvi)
#commands.getoutput(mkpdf)
#commands.getoutput(rmfile)
print ("finished!")
