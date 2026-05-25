import discord
from discord.ext import commands
import json
import random

with open('config.json') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
PREFIX = config['prefix']
NAME = config['name']
DELTIME = config['deltime']
THEME = config['theme']
WEBSITE = config['website']


random_citation = [
    "L’amour te construit, mais parfois c’est lui qui t’apprend la force.",
    "Ne baisse jamais la tête, sauf pour regarder ton prochain pas.",
    "Les larmes ne font pas de toi quelqu’un de faible, elles prouvent que tu ressens encore.",
    "Quand tout s’effondre, rappelle-toi que tu t’es déjà relevé.",
    "La motivation vient et repart, la discipline reste.",
    "L’amour n’est pas toujours doux, mais il est toujours vrai.",
    "Le silence est parfois la réponse la plus bruyante.",
    "Force à toi, même quand personne ne voit tes efforts.",
    "Si tu veux changer ta vie, change tes habitudes.",
    "Aimer, c’est risquer. Ne pas aimer, c’est se perdre.",
    "La rue t’apprend vite : personne ne te donnera ce que tu ne vas pas chercher.",
    "Le cœur se casse, mais l’âme recolle les morceaux.",
    "Tu vaux plus que ce que tes doutes te racontent.",
    "Un jour tu comprendras pourquoi tu as dû perdre certaines personnes.",
    "Les vrais gagnants travaillent pendant que les autres dorment.",
    "N’aie pas peur d’être seul, c’est là que tu te construis.",
    "Chaque douleur t’a rendu plus solide que tu ne crois.",
    "Les sentiments compliquent tout, mais ils rendent vivant.",
    "Si tu n’avances pas, personne ne viendra te pousser.",
    "La jalousie parle toujours plus fort que la vérité.",
    "Aime sans regret, quitte sans haine.",
    "Quand c’est dur, c’est que tu deviens meilleur.",
    "Le cœur garde des cicatrices invisibles.",
    "Rêve grand, même si on se moque de toi.",
    "Parfois tu te perds pour mieux te retrouver.",
    "Donne-toi la force que personne ne pense que tu as.",
    "La loyauté n’a pas de prix.",
    "Les choses simples donnent les émotions vraies.",
    "L’avenir appartient à ceux qui refusent d’abandonner.",
    "Aimer c’est facile, rester c’est courageux.",
    "La douleur forge des guerriers silencieux.",
    "Le monde appartient à ceux qui osent.",
    "Ne force rien : ce qui est vrai reste.",
    "Tu n’es pas fatigué, tu es proche du niveau suivant.",
    "Les liens deviennent toxiques quand tu t’oublies.",
    "Un seul bon choix peut changer toute une vie.",
    "Aime-toi assez pour ne pas courir derrière ce qui fuit.",
    "La patience est une forme de force.",
    "On guérit lentement, mais on guérit vraiment.",
    "Si tu savais ce dont tu es capable, tu arrêterais d’hésiter.",
    "La motivation te lance, l’habitude te porte.",
    "Certains sourires cachent des tempêtes.",
    "Ne regrette pas ce qui t’a appris.",
    "L'amour n'est pas un refuge, c'est un voyage.",
    "Le respect, ça se gagne, ça ne se réclame pas.",
    "La solitude n’est pas vide, elle est juste silencieuse.",
    "Tu n’échoues pas, tu apprends à réussir.",
    "Les vraies forces ne font pas de bruit.",
    "Tes efforts finiront par parler pour toi.",
    "Tu mérites quelqu’un qui ne joue pas avec ton âme.",
    "Rien n’est plus puissant qu’un esprit décidé.",
    "Ne laisse pas la peur diriger tes choix.",
    "Chaque nuit sombre porte un matin différent.",
    "La drill, c’est pas que du bruit, c’est le cri de ceux qu’on n’écoute pas.",
    "Tu peux pleurer, mais avance quand même.",
    "Ce que tu veux, veux-le vraiment.",
    "La vie teste toujours les plus courageux.",
    "L’amour est beau, mais il ne doit jamais te détruire.",
    "Le manque rend fou, mais la patience apaise.",
    "Si tu savais tout ce qui t’attend, tu continuerais sans douter.",
    "Quand tu veux tout abandonner, souviens-toi pourquoi tu as commencé.",
    "Ne dis rien, montre tout.",
    "La douleur change les gens, parfois trop.",
    "Les promesses vides laissent les cœurs pleins de vide.",
    "T’attaches pas à ceux qui se détachent de toi.",
    "Ton futur te remerciera pour ta discipline d’aujourd’hui.",
    "Chaque rupture fait renaître une version plus forte de toi.",
    "La rue ne pardonne pas, mais la vie non plus.",
    "Si tu veux la paix, fais le ménage dans ta vie.",
    "Un cœur pur attire toujours mieux qu’un visage joli.",
    "Ne laisse pas ton passé t’empêcher de devenir grand.",
    "Aime tant que tu peux, mais jamais au point de t’effacer.",
    "Le succès arrive quand tu refuses d’abandonner.",
    "Les sentiments vrais ne disparaissent pas, ils se transforment.",
    "Tes défauts ne t’empêchent pas d’être incroyable.",
    "Sois ton propre pilier quand tout tremble.",
    "Les gens parlent, les résultats répondent.",
    "Le manque de courage détruit plus de rêves que l’échec.",
    "La douleur du présent construit la force du futur.",
    "Aimer, c’est offrir de la vulnérabilité.",
    "Ne confonds pas l’amour et l’habitude.",
    "Le monde ne te doit rien, mais tu te dois beaucoup.",
    "La vérité finit toujours par percer, même dans le noir.",
    "Ton cœur mérite la paix, pas le chaos.",
    "Chaque jour est une page neuve, écris mieux.",
    "La rancune pèse, le pardon libère.",
    "La vie frappe fort, mais tu frappes plus fort.",
    "Tu n’as pas besoin d’être parfait pour être aimé.",
    "Le mental, c’est 80 % du chemin.",
    "Tout ce que tu veux commence par croire que tu le mérites.",
    "La tristesse t’ouvre les yeux que la joie fermait.",
    "Qui t’aime vraiment ne te laisse jamais douter.",
    "Le temps révèle tout, même les intentions.",
    "Travaille en silence, brille en plein jour.",
    "Ce que tu traverses maintenant te rendra méconnaissable demain.",
    "La force n’est pas de ne jamais tomber, mais de toujours revenir.",
    "La vie est courte, choisis ce qui t’élève."
]



async def setup(bot):
    @bot.command()
    async def citation(ctx):
        citation = random.choice(random_citation)
        await ctx.message.edit(content=f"""
{THEME} **[❃ {NAME} ❃ - Citation]({WEBSITE})**
{THEME} **Citation** >> {citation}
""")



