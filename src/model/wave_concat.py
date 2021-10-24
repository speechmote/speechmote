import wave

infiles = ["src/model/groot1.wav", "src/model/groot2.wav", "src/model/groot3.wav"]
outfile = "src/model/iamgroot.wav"

data = []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
    
output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()
