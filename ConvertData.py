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
data = pd.read_csv("haplotypes.csv")
locations = pd.read_csv("alleleData.csv")

## EXMAPLE: sample_data.add_site(position=1, genotypes=[0, 0, 1, 0], alleles=["G", "C"])

sample_data = ts.SampleData(path="testts.samples")

nsites = len(locations.index)
def createSampleData(data, locations) :
    for x in range(0, nsites):
        position = locations.iloc[x,1] # position is the xth row of column 2 of locations DF
        genotypes = data.iloc[x,2:] # genotype is the xth row of column 3:N of the data DF
        genotypes = genotypes.tolist() # genotypes must be list
        alleles = locations.iloc[x,2] # alleles are the xth row of column 3 of the locations dataframe
        allele1 = alleles[1:2]
        allele2 = alleles[3:4]
        alleles = [allele1,allele2]

        sample_data.add_site(position=position, genotypes=genotypes, alleles=alleles)

    sample_data.finalise()
