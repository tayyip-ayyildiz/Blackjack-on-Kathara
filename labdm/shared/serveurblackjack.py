#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import random


users=[]
table =[]
tableEncours=[]
tableTemp=[]
numeroT=0;

def blackjackServ(LC, LM, table):
	
	
	somme=0
	
	for i in LM:
		
		if(i=="J" or i=="D" or i=="K"):
			
			somme+=10;
		
		else:	
			
			somme+=i;
			
	while(somme<17):
	
		
		i=random.choice(LC);
			
		while(i==[]):
			
			i=random.choice(LC);
				
		j=random.choice(i);

		if(j!="J" and j!="D" and j!="K"): 
				
			k=int(j);
				
		else:
				
			k=12;

		if(k==1):
						
			if(somme<11):
							
				LM+=[11];
				i.remove(j)
							
				somme=0;
							
				for i in LM:
			
					if(i=="J" or i=="D" or i=="K"):
			
						somme+=10;
		
					else:	
			
						somme+=i
						
			else:
					
				LM+=[1];
				i.remove(j)
							
				somme=0;
							
				for i in LM:
			
					if(i=="J" or i=="D" or i=="K"):
			
						somme+=10;
		
					else:	
			
						somme+=i;
						
		elif(k==12):

			LM+=[j];
			i.remove(j);
						
			somme=0;
						
			for i in LM:
			
				if(i=="J" or i=="D" or i=="K"):
			
					somme+=10;
		
				else:	
			
					somme+=i;
						
		else:
			
			LM+=[k];
			i.remove(j);
						
			somme=0;
						
			for i in LM:
			
				if(i=="J" or i=="D" or i=="K"):
			
					somme+=10;
		
				else:	
			
					somme+=i
	
	res=somme
	somme=0;
	return res
	


async def blackjack(LM,table,writer,reader):
	LC1=table[3]
	tout=table[5]
	continu=True
	addr = writer.get_extra_info('peername')[0]
	
	while(continu):
    	
		data = await reader.readline()
		writer.write(data)
		if(data.decode()[0]=="M"):
			
			if(data.decode()[-3]=="1"):
				
				somme=0;
							
				for i in LM:
			
					if(i=="J" or i=="D" or i=="K"):
			
						somme+=10;
		
					else:	
			
						somme+=i;
				
				i=random.choice(LC1);
			
				while(i==[]):
			
					i=random.choice(LC1);
				
				j=random.choice(i);

				if(j!="J" and j!="D" and j!="K"):
				
					k=int(j);
				
				else:
				
					k=12;

				if(k==1):

					writer.write(("Vous avez piochez la carte : "+str(j)).encode()+b"\r\n");
					writer.write("Vous êtes tombé sur un AS".encode()+b"\r\n");
						
					if(somme<11):
							
						LM+=[11];
						i.remove(j)
							
						somme=0;
							
						for i in LM:
			
							if(i=="J" or i=="D" or i=="K"):
			
								somme+=10;
		
							else:	
			
								somme+=i;
						
						writer.write(("Votre main : "+str(LM)+" TOTAL : "+str(somme)).encode()+b"\r\n")
						writer.write(("La premiere carte du donneur : "+str(tout[0][1][0])).encode() + b"\r\n")
						
						if(somme<=21):
							
							writer.write('.'.encode()+b"\r\n")
						
						else:
							
							writer.write(("Le joueur "+addr+" à dépasser 21, il est disqualifié").encode()+b"\r\n")
							
							if(table[2]==1):
								
								for z in range(len(tout)):
									
									if(tout[z][0]=="serveur"):
										
										serv=blackjackServ(LC1,tout[z][1],table)
											
										if(serv<=21):
			
											tout[z][1]=serv
											break
											
										else:	
												
											tout.pop(z)
											break
							
							table[2]-=1
							
							
							writer.write("END".encode()+b"\r\n")
							continu=False
					else:
						
						LM+=[1];
						i.remove(j)
							
						somme=0;
							
						for i in LM:
			
							if(i=="J" or i=="D" or i=="K"):
			
								somme+=10;
		
							else:	
			
								somme+=i;
						
						writer.write("Votre main :".encode()+b"\r\n")
						writer.write(str(LM).encode()+b"\r\n")
						writer.write(("TOTAL : "+str(somme)).encode()+b"\r\n");
						writer.write(("La premiere carte du donneur : "+str(tout[0][1][0])).encode() + b"\r\n")
						
						if(somme<=21):
							
							writer.write('.'.encode()+b"\r\n")
						
						else:
							
							writer.write(("Le joueur "+addr+" à dépasser 21, il est disqualifié").encode()+b"\r\n")
							
							if(table[2]==1):
								
								for z in range(len(tout)):
									
									if(tout[z][0]=="serveur"):
										
										serv=blackjackServ(LC1,tout[z][1],table)
											
										if(serv<=21):
			
											tout[z][1]=serv
											break
											
										else:	
												
											tout.pop(z)
											break
							
							table[2]-=1
								
							writer.write("END".encode()+b"\r\n")
							continu=False

				elif(k==12):

					writer.write(("Vous avez piochez la carte : "+str(j)).encode()+b"\r\n");
					LM+=[j];
					i.remove(j);
						
					somme=0;
						
					for i in LM:
			
						if(i=="J" or i=="D" or i=="K"):
			
							somme+=10;
		
						else:	
			
							somme+=i;
						
					writer.write("Votre main :".encode()+b"\r\n")
					writer.write(str(LM).encode()+b"\r\n")
					writer.write(("TOTAL : "+str(somme)).encode()+b"\r\n");
					writer.write(("La premiere carte du donneur : "+str(tout[0][1][0])).encode() + b"\r\n")
						
					if(somme<=21):
							
							writer.write('.'.encode()+b"\r\n")
						
					else:
							
						writer.write(("Le joueur "+addr+" à dépasser 21, il est disqualifié").encode()+b"\r\n")
						
						if(table[2]==1):
								
							for z in range(len(tout)):
									
								if(tout[z][0]=="serveur"):
										
									serv=blackjackServ(LC1,tout[z][1],table)
											
									if(serv<=21):
			
										tout[z][1]=serv
										break
											
									else:	
												
										tout.pop(z)
										break
						
						table[2]-=1
								
						writer.write("END".encode()+b"\r\n")
						continu=False

				else:
					
					writer.write(("Vous avez piochez la carte : "+str(j)).encode()+b"\r\n");
					LM+=[k];
					i.remove(j);
						
					somme=0;
						
					for i in LM:
			
						if(i=="J" or i=="D" or i=="K"):
			
							somme+=10;
		
						else:	
			
							somme+=i;
						
					writer.write("Votre main :".encode()+b"\r\n")
					writer.write(str(LM).encode()+b"\r\n")
					writer.write(("TOTAL : "+str(somme)).encode()+b"\r\n");
					writer.write(("La premiere carte du donneur : "+str(tout[0][1][0])).encode() + b"\r\n")
						
					if(somme<=21):
							
							writer.write('.'.encode()+b"\r\n")
						
					else:
							
						writer.write(("Le joueur "+addr+" à dépasser 21, il est disqualifié").encode()+b"\r\n")
						
						if(table[2]==1):
								
							for z in range(len(tout)):
									
								if(tout[z][0]=="serveur"):
										
									serv=blackjackServ(LC1,tout[z][1],table)
											
									if(serv<=21):
			
										tout[z][1]=serv
										break
											
									else:	
												
										tout.pop(z)
										break
						
						table[2]-=1
								
						writer.write("END".encode()+b"\r\n")
						continu=False
					
					
				
			else:
				
				somme=0;
				
				for i in LM:
				
					if(i=="J" or i=="D" or i=="K"):
				
						somme+=10;
			
					else:	
						somme+=i;
				
				writer.write("Votre main :".encode()+b"\r\n")
				writer.write(str(LM).encode()+b"\r\n")
				writer.write(("TOTAL : "+str(somme)).encode()+b"\r\n");
				tout.append([addr,somme])
				
				if(table[2]==1):
								
					for z in range(len(tout)):
									
						if(tout[z][0]=="serveur"):
										
							serv=blackjackServ(LC1,tout[z][1],table)
											
							if(serv<=21):
								
								tout[z][1]=serv
								break
											
							else:	
												
								tout.pop(z)
								break
					
				table[2]-=1
					
				while(table[2]!=0):
					
					await asyncio.sleep(0.1)
				
				writer.write(qui(tout).encode()+b"\r\n")
				writer.write("END".encode()+b"\r\n")
				continu=False
	
	
	
	
def qui(total):

	global tableEncours
	
	res=[]
	
	for t in total:
		
		res.append(t[1])
	
		
	if(len(res)==0):
	
		return "Aucun gagnant"
	
	else:
	
		nb=max(res)
		ind=res.index(nb)
		
		
		if(res.count(nb)>1):
			
			eg=[]
			
			for t in range(len(res)):
				
				if(res[t]==nb):
				
					eg.append(total[t][0])
				
			return ("Egalite entre les joueurs : "+str(eg)+" avec un score de : "+str(nb))
			
			total.clear()	
		
		else:
		
			return("Le gagnant est : "+str(total[ind][0])+" avec un score de : "+str(nb))
			
			total.clear()
				

	
	

async def handle_requestCroupier(reader, writer):
	addr = writer.get_extra_info('peername')[0]
	message = f"Croupier {addr} is connected."
	print(message)
	msg="Bienvenue"
	writer.write( msg.encode()+ b"\r\n")
	global numeroT
	total=[]
	cartes=[["1","2","3","4","5","6","7","8","9","10","J","D","K"],["1","2","3","4","5","6","7","8","9","10","J","D","K"],["1","2","3","4","5","6","7","8","9","10","J","D","K"],["1","2","3","4","5","6","7","8","9","10","J","D","K"]]
	continu=True
	while(continu):
    	
		data = await reader.readline()
		writer.write(data)
		if(data.decode()[0]=="N" or data.decode()[0]=="T"):
			
			writer.write(data)
			tableTemp.append(data.decode().strip())
			
			if(data.decode()[0]=="T"):
				continu=False;
    	
	
	for t in range(len(tableTemp)-1):
		
		table.append([tableTemp[t].split(' ')[1],tableTemp[t+1].split(' ')[1],0,cartes,numeroT,total])
		numeroT+=1;

	for u in table:
		
		print("\nLa table",u[0],"avec un temps d'attente de : ",u[1])
	
	del tableTemp[:]
	writer.close()

async def handle_requestJoueur(reader, writer):
	addr = writer.get_extra_info('peername')[0]
	users.append(writer)
	message = f"Joueur {addr} is connected."
	print(message)
	msg="Bonjour voici les tables disponible : "
	for t in range(len(table)):
		msg=msg+table[t][0]+', '
	writer.write( msg.encode()+ b"\r\n")
	main=[]
	existe=False
	global tableEncours
    		
	data = await reader.readline()
	if(data.decode()[0]=="N"):
				
		n=data.decode()[5:len(data.decode())-2]
		if(len(table)==0):
				
			print("Aucunes tables disponibles\n")
			writer.write("END".encode() + b"\r\n")
				
		else:
				
			for t in table:
				
				if t[0]==n:
					existe=True	
					messa = f"Joueur {addr} join the table : "+n+"\n"
					print(messa)
					if t[2]>0:
						for u in tableEncours:
							if(u[0]==n):
								u[2]+=1
						while(t[6]):
							await asyncio.sleep(0.1)
						break;
					
					else:
						t[2]+=1
						tableEncours.append(t)
				
						t[5].append(["serveur",[]])
						t.append(True)
						t.append(0)
									
						for o in range(2):
								
							i=random.choice(t[3]);
								
							while(i==[]):
								
								i=random.choice(t[3]);
									
							j=random.choice(i);
									
							if(j!="J" and j!="D" and j!="K"): 
									
								k=int(j);
									
							else:
									
								k=12;
										
							if(k==1):
											
								somme=0;
								
								for p in t[5][0][1]:
									
									if(p=="J" or p=="D" or p=="K"):
									
										somme+=10;
								
									else:	
												
										somme+=p;
											
								if(somme<11):
														
									t[5][0][1].append(11);
									i.remove(j)

								else:
											
									t[5][0][1].append(1);
									i.remove(j)


							elif(k==12):

								t[5][0][1].append(j);
								i.remove(j);

							else:
											
								t[5][0][1].append(k);
								i.remove(j);
						
						await asyncio.sleep(int(t[1]))
						t[6]=False
						break;
				
						
	if(existe==False):			
		print("La table : ",n,"n'existe pas \n")
		writer.write("END".encode() + b"\r\n")				
	if(existe==True):
		
		
		for t in range(len(table)):
			
			if(table[t]!=[] and table[t][0]==n):
			
				del table[t]
				break
		

		await asyncio.sleep(0.5)
		
		for w in tableEncours:
			
			if(w[0]==n):
			
				for s in range(2):   #draw 2 cards for each players
			
					i=random.choice(w[3]);
			
					while(i==[]):
			
						i=random.choice(w[3]);
				
					j=random.choice(i);
				
					if(j!="J" and j!="D" and j!="K"): 
				
						k=int(j);
				
					else:
				
						k=12;
					
					if(k==1):
						
						somme=0;
				
						for q in main:
				
							if(q=="J" or q=="D" or q=="K"):
				
								somme+=10;
			
							else:	
							
								somme+=q;
						
						if(somme<11):
							
							main.append(11);
							i.remove(str(j))

						else:
						
							main.append(1);
							i.remove(str(j))


					elif(k==12):

						main.append(j);
						i.remove(str(j));

					else:
					
						main.append(k);
						i.remove(str(j));	
		
		somme=0;
							
		for i in main:
			
			if(i=="J" or i=="D" or i=="K"):
			
				somme+=10;
		
			else:	
			
				somme+=i;
						
		writer.write(("Votre main : "+str(main)+" TOTAL : "+str(somme)).encode()+b"\r\n")
		
				
		for s in tableEncours:
		
			if(s[0]==n):
			
				while(s[7]!=52-2*(s[2]+1)): #wait until other players draw their 2 cards
				
					s[7]=0
				
					for h in s[3]:
								
						s[7]+=len(h)
					
					await asyncio.sleep(1)
										
		res=0;
							
		for r in tableEncours:
		
			if(r[0]==n):
				
				for i in r[3]:
					
					for j in i:
			
						res+=1;
						
		writer.write((" Il reste : "+str(res)+" cartes").encode()+b"\r\n")
		
				
		for w in tableEncours:
			
			if(w[0]==n):
			
				
				writer.write(("La premiere carte du donneur : "+str(w[5][0][1][0])).encode() + b"\r\n")
				writer.write(".".encode() + b"\r\n")
				await blackjack(main,w,writer,reader)
				
	
	await asyncio.sleep(1)
	
	for f in tableEncours:
		
		if(f[0]==n and f[2]==0):
			
			f.clear()
			tableEncours=list(filter(None,tableEncours))	
			break
	
		
	
	writer.close()


async def serveurblackjack():
    # start a socket server
    server = await asyncio.start_server(handle_requestCroupier, '0.0.0.0', 668)
    server2 = await asyncio.start_server(handle_requestJoueur, '0.0.0.0', 667)
    addr = server.sockets[0].getsockname()
    addr2 = server2.sockets[0].getsockname()
    print(f'Serving on {addr} and {addr2}')
    users.append([server2,0])
    
    async with server:
        await server.serve_forever() # handle requests for ever

if __name__ == '__main__':
    asyncio.run(serveurblackjack())






