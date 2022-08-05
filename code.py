
packageList = ['78','78','4C','FC','BC','D6','0F','A3','0D,'0A']

               
n = 4    #in my case my retun is with 4 characters 

checksumData = checksumDataFormat(packageList)  #transformando o package para o modelo de calculo do CRC                
checksumCalculated = (GetFormattedHex(GetCrc16(checksumData), n))



def GetFormattedHex(intNum, lenOfHexString):
	return format(intNum, "0" + str(lenOfHexString) + "x").upper() 


def checksumDataFormat(packageList):
    packageChecksum = packageList[:-4]         #remove os 4 ultimos bytes (0D 0A e CRC)
    packageChecksum = packageChecksum[2:] #remove os dois primeiro bytes (startBit)
    packageChecksum = convertListToString(packageChecksum)  #transforma em uma string o pacote a ser calculado o CRC
 
