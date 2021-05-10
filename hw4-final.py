from Bio import SeqIO

#1
def my_own_fasta_parser(inFile):
    sequences = {}
    for line in SeqIO.parse(inFile, "fasta"):
        #sequences[seq.id] = seq.seq
        id = int(line.id[3:])
        seq = str(line.seq)
        sequences[id] = seq
    return sequences

print(my_own_fasta_parser("/Users/maria/Desktop/M4135/pythonProject/prot.fasta"))

#2
def my_own_residue_abundance(input_file, residue, threshold=0.2):
    seq_ids = []
    sequences = my_own_fasta_parser(input_file)
    for seq_id, sequence in sequences.items():
        result = sequence.count(residue)
        th = result/len(sequence)
        if th > threshold:
            seq_ids.append(seq_id)
    return seq_ids

print(my_own_residue_abundance("/Users/maria/Desktop/M4135/pythonProject/prot.fasta", "F"))

#3
from Bio.Seq import Seq
mdna = Seq("AGTACTAGAGCATTCTATGGAG")
dna = mdna.tomutable()

while len(dna) % 3 != 0:
    dna.append("N")

dna = dna.toseq()
pept = dna.translate()

#4
def rev_compl_one_line(seq):
    return ("".join(reversed([("T" if s == "A" else ("A" if s == "T" else ("G" if s == "C" else ("C" if s == "G" else s)))) for s in seq])))

print(rev_compl_one_line("AACGT"))
