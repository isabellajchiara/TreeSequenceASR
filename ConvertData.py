# Install
# SampleData object will be passed to tsinfer.infer command

# Create SampleData object:
    # add data for each site one by one using SampleData.add_site()
    # arg1 = position of site in genome coordinates
    # arg2 = list of genotypes for the site
    # arg3 = list of alleles
    # arg4 = index in the allele representing the ancestral state

import tsinfer as ts 
import pandas as pd
data = pd.read_csv("haplotypes.csv") #import haplotypes. a matrix of haplotypes, from ASR, each col is a SegSite
geno = data.transpose() #each row is a SegSite
geno.drop(index=geno.index[:2], axis=0, inplace=True) #remove first two rows of identifying information
locations = pd.read_csv("alleleData.csv") #contains morgans and alleles of each SegSite

## EXAMPLE: sample_data.add_site(position=1, genotypes=[0, 0, 1, 0], alleles=["G", "C"])

sample_data = ts.SampleData(path="testts.samples")

nsites = len(locations.index)
def createSampleData(geno, locations) :
    for x in range(0, nsites):
        position = locations.iloc[x,2] # position is the xth row of column 2 of locations DF
        genotypes = geno.iloc[x,:] # row = locus. entire row = state at that locus for every obs.
        genotypes = genotypes.tolist() # genotypes must be list
        alleles = locations.iloc[x,3] # alleles are the xth row of column 3 of the locations dataframe
        allele1 = alleles[1:2]
        allele2 = alleles[3:4]
        alleles = [allele1,allele2]

        sample_data.add_site(position=position, genotypes=genotypes, alleles=alleles)

    sample_data.finalise()
