# load libraries
import requests
from flask import Flask,jsonify,request,send_file
import spacy
from spacy import displacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import re

# nltk.download('stopwords')
# nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def rem_stop_words(string):
  word_tokens = word_tokenize(string)
  filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
  return ' '.join(filtered_sentence)

def hash(text):
  text = str(text)  
  try:
      doc = nlp(text.lower())
  except:
      doc = nlp(text)
  hash_tags=[]
  for np in doc.noun_chunks:
    hash_tags.append(np.text)
  for ent in doc.ents:
      hash_tags.append(ent.text)

  key_hash = rem_stop_words(", ".join(hash_tags))
  key_hash = list(set(key_hash.replace(" ,",",").split(', ')))
  filet_list=["week","made","note","shut","wearing","obsessive","behind","prepared","asked","need","talking","best","match","considering","rips","part","matching","stepped","tablet","showing","trick","using","explain","curiosity","charge","satisfying","assigned","overhead","notified",'watch','miyu','jerome','telling','chick','reacts','quietly','crone','story','boring','seek','grab','stare','wooden','ground','issue','toss','creek','watching','enjoy','rica','control','seem','help','adam','physical','weatherby','problem','found','spot','suddenly','release','slow','slightly','angrily','idiot','loss','word','continued','around','wake','center','noted','fall','result','realizing','change','understand','staircase','solid','awoke','accepted','thinking','tablet','charlie','complain','home','make','previous','charge','satisfying','match',"previous","pick","weird","else","endure","if","sincerely","noticing","somehow","stared","yesterday","together","certain","hover","think","tend","seat","feel","leaf","cream","lightly","nerve","trickle","choice","freely","here","nose","flashlight","notch","notice","show","flow","mine","giggle","bathroom","checked","catch","pocket",'familiar','adaptation','content','longer','stop','plea','indiscriminately',"onward",'sickeningly',"focus","consume","strain","shower","ineffective","spite","ease","range","controlled","expected","shriek","hesitation","taste","outbreak","instantly","","side","doubt","fixed","taking","mass","throne","period","known","slump","wood","crack","obviously","forth","series","third","fifth","six","sixth","five","seven","eight","nind","ten","proper","thud","sinew","twist","cradling","instantaneous","seemingly","apart","watched","beautiful","half","snap","accompanied","starting","relaxed","people","extremely","welcoming","important","severe","instinctively","count","friendly","welcome","often","stay","somewhat","mention","knife","today","cheap","however","case","pair","otherwise","somewhat","everywhere","comfortable","exact","glass","feeling","felt","bringing","ignore","part","small","annoying","afterwards","online","admire","talk","sprint","also","sweet","white","only","pretty","sitting","roll","black","loud","bastard","finger","","quiet","complete","short","dirt","purpose","gesture","shed","sigh","jerk","crate","shoulder","somewhere","empty","turn","freshly","mound","shovel","area","hard","soft","frantically","wide","probably","field","rest","knee","minute","decade","heart","volume","soon","feed","open","grinning","close","coming","crushing","seen","crush","face","device","hair","foot","matted","smile","lipstick","looking","upstairs","blade","increasingly","occasionally","knelt","table","look","hold","test","point","progress","lowered","negative","uniformed","chair","anywhere","maybe","rephrase","cross","blink","hypnotic","rough","search","squirmed","probe","neck","artery","tilt","sinking","limb","throat","pulse","chin","tongue","brain","unable","kind","front","mind","opened","afford","second","there","answer","sorry","evening","tapped","shaken","keeping","matter","quickly","pearly","flesh","slowly","convincing","talked","silence","passed","convincing","alternative","response","gate","inside","outside","relentlessly","many","example","common","minor","true","false","completely","apple","mouth","wrenched","know","monday","tuesday","wednesday","thursday","friday","saturday","sunday","dusty","forever","followed","plan","original","manage","putting","handed","take","favorite","forward","worried","awhile","sometimes","inch","putting","picked","guess","almost","refuse","hour","month","still","real","fell","stretch","reach","slowly","laughter","joyfully","happy","definition","displaying","number","repeatedly","really","tired","insanity","aloud","saying","simple","thing","meant","just","tell","closed","lead","wrong","stair","thing","stoplight","grey","right","orangish","door","move","plenty","body","disposed","retreat","find","start","plate","downstairs","steamy","greasy","even","yup","mean","going","confine","outline","closed","brutal","bro","list","date","dreary","standing","venture","rush","ordinary","early","hand","final","beeped","left","spectrum","professor","scout","reality","yellow","kid","colored","reason","power","fate","intense","red","based","basically","class","finally","sense","potential","year","tends","fair","reflection","full","sort","hope","different","live","green","sickening","sence","aura","glow","crash","end","numbered","amount","fired","later","fresh","morning","motif","young","t","clutching","burining","pain","fried","gently","excitedly","chest","fruit","breakfast","shaking","floor","courage","place","bath","safe","hours","terrible","spread","hastily","wire","razor","huge","confused","squirming","spasmed","leave","particularly","filled","insect","distance","screaming","tap","back","slide","always","s","hesitant","properly","bad","chance","doctor","boredom","cat","far","normalcy","care","dad","little","park","undammed","pointing","easy","gouged","charming","duration","mom","data","likely","replaced","away","dark","dishwasher","ready","fake","baby","sparingly","several","street","constantly","vitamin","toy","bored","parent","wall","sure","next","scene","name","game","naturally","night","paper","section","bedroom","kinda","new","corner","skin","name","getting","room","actually","day","ceiling","converting","removal","piece","peeling","papered","sunburn","am","instance","ma","person","material","similar","enough","peel","removing","already","oddly","removed","man","head","much","tenth","licked","indeed","use","wife","world","knowing","wristwatch","work","well","too","ever","syndrome","dog","then","moment","life","old","smiled","instead","long","time","forehead","eventually","wisely","overjoyed","fact","boy","eye","last","exactly","used","first","son","alive","pat","good","boy","girl","girls","boys"]
  filet_list = filet_list + ['zero','one','two','three','four','five','six','seven','eight','nine']
  for i in key_hash:
    if i in filet_list:
      key_hash.remove(i)
  key_hash = [i.replace(',','').strip() for i in key_hash]
  key_hash = [item for item in key_hash if not item.isdigit()]
  key_hash = ["#"+item for item in key_hash]

  return key_hash

@app.route('/TagsGenerator',methods=['POST'])  #main function
def main():
    params = request.get_json()
    input_query=params["Text"]
    response = hash(input_query)

    return jsonify({"Hash Tags":response})     

if __name__ == '__main__':
    app.run()             