import math
from itertools import count, islice
# Given a string, find the length of the maximum length palindromic sub string .
# Suppose 'l' is the length of maximum length palindromic sub string, check whether 'l' is prime number or not,
# if it is prime ,then print 'PRIME' else 'NOT PRIME'.
#
# SAMPLE INPUT
# 3
# aabaaz
# aavsba
# ghsdffssff
#
# SAMPLE OUTPUT
# PRIME
# PRIME
# NOT PRIME

# palindromeLength() returns -1 if not a palindrome and an integer length if it is
# for i, l in enumerate(word)
#   if palindromeLength != -1
#     for j in word
#       max = palindromeLength(word[i:j]

def is_max_palindrome_prime(word):
    max = -math.inf
    memo = dict()
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            current_palindrome_length = palindrome_length(word[i:j], memo)
            if current_palindrome_length != -1:
               if max < current_palindrome_length:
                   max = current_palindrome_length
            else:
                break
    is_prime(max)


def is_prime(n):
    if n > 1 and all(n%i for i in islice(count(2), int(math.sqrt(n)-1))):
        print("PRIME")
    else:
        print("NOT PRIME")

def palindrome_length(word, memo):
    if word in memo:
        return memo[word]
    if list(word) == list(reversed(word)):
        memo[word] = len(word)
        return len(word)
    else:
        return -1

is_max_palindrome_prime("qeltuiosytrabycsnvdourrbvarooaqhgdaaoovmkonlnrdcpirjckkxkbnydffklhmzwhngyctnuzpjjislsfleiyfmgkwrskqqufysirfeqwnchhnbmygvzlhfxfwrrohltfddzkhrhutqejrqhxnikuniblztzjevqkyruijdcetinnzxkmfvjvfmgghirodiydbulmaqrvygizfvolsxizlqftaxjfhhjidwvfmodnwnocicpcbxbnpjiqirvpagzfdwlrmqgjdvloxaqzxuoodwelnccnidsnaffmvnvzigpigfhfbxuetaricvxlzrybxfnutlvdrklasuhtrdaketsgprtqjurizecurayjklleguyxyaketemkwgaharpbytwptwaghnkpiknikzmgdaszgtgimxkmriekggqpubfenuoytcgwcyyjtgtiefuvpahvhylbbshqmvofxwbbxzmqigamlvhbxqyeqlhtdokplawixymuzymhenvskethvtmlftfiipatpweowqkwoxfvkdnuhidcbpqglvrtmrodpuummekdbrynuljcvngwewfptwkhpblevhqilcnpulcoyoqtdxrhvwxpuhyjklqgsiqeldvfqztonmjqlaygzxxtgwfrhvzadpgoudtmcpaqblimlgumfsgmqlfzieblvjcrmxdpmffpqnddwyqdswpkjwjralexugojetysyfiquluslmwdknntkzmmmqkixardwpvwwfnrrjjcvfiftxadymrkcbtbemgcceyyjlrcubfrgpwboygnkyxpzssffzhjdgjotbrqcyhkngmdesqpqqgskyzpzjacpkrkliapikbvqnywirlahtursujrdjwuvpeizhxhrzejocfyvtzemvygrhyuswqqlxykeytxzxgnbloxepbtkzzcixybvrtgorsupnrqkzgmmujrjmmvmlzulyxgpqpfkjzbxsshtyvfsgydtkahwadhadnpvewfovhlpzuizsntamyvyycuyibylrpgvlolivyxwthvnxqnlojjmnenvhniadpyqfjbaiyydivqflfqzqznefabpokptbplgzmijngmvbeaolsnctagbdhqtthmuxzaymkhzqvwtbwhmquojxwmcgcvzkjwjiyhujovzlrtmpaafxrrwndyvitvuctdmrkhaaeclwxzlzztwqmserqbzlyvnryajkjlknpxlmwxmwskmedsvvuxhsswktyvdjiqxynikmhyizjwfordllasfurrnporbxhyvwihisisttpzhgestenaygsoxgfyfoyckjmtbulwncvwkzqfffgglaulibjopiqztcuuyiqnkojvpaaxfidtizeranfpxxqsclmatfofvzckzfjhnmaylgplvwcvttnxgcabjqieplqrsayhmafaiundssyololtqlwzbedtrvkjvktkmymuvzznrabeonzeavdecixtdjfbtynhyzdtachuckaszawaxbezldtrmashyhqwitsixzeclfulfrlcurcgwxxkxrrxajvicpqzqvbcawnhpallrnrpmqzljqkjzirdxkeohgqjefsvfdgytanfsmteednfnhiltmbcutnayfvdieddgqjycecgjsnxbvkwjlyegleescjagmeoepmgvroelbdmynkhainivumnwxpeltspkgxfxnmkqpwofgyhqlqnfeadcqhplbfykefjsruihszozxvrilfqshtuzdjlgqlqxqapiwzroyhnxchgqmyivtevwpifitvfjxwttvmiwtxtyeboszyotclrrtwzmsgxrctlyfvubspzzrntqnjjpubinxkbrqzltsytztpanezovoimbrxsoabbandrdecyyarxvgajlbzishuvbuopursuexohbsgztzzqgzztabbuiyqlsecoxvjbsxkwpsxkswbaxcvadwuowkzqqcfnzqqtpbpetnrnlunlyilehhsfstwkxdywtqsirjonyhakbqvaaiejpypjrnurquplkhverjrprtbujyukgatyakhuxdlpzcamkvqdhjsyewsoupadrtbsgkodoztpbvbnrtqyelyjjszdjzgbujvaujekkzznudbnytndgnopintrobuilrjhcprmqscmvdawypzffpuncpeqtbagslnvagjsylfwqhsrwtwbisqmkvedyejqqynsezlcmqadzuuvnszxmplwmpbkwkdoiqgorttelthkqdidxhdlyqinglxewcsgvavmuoqhjzszeafdjkpjazwikwmiygrthoidcyknacpeeuipgzzgyvrirdtsmkntyvycwipwngctcmjilirjfiuxnnrbzeuxcszydqwsxalbnukacdminghcvaeueytitugykeqjfbnuyxuacgkpotrjtvfywagruprhvhsakfuieplgxvxmppvimdikdrbaishdbbgmhawlrhupfrbwiygvdphjijjqdsvhtbvceroxbkogbpckqihtzoejzpbfhxodajfecvedfsljkpvaacvbsclurmbzjpemalschwioptxblsdlwymrcxnukovvfzhfkajtyrinnhqyctlauxrwxeqjulgbmogzqquojeewmuuoqfokfigcoznlmtmzjvazluqubwtnqpdgvtscdzgsytfkorlymnzzkpwllpyeedmbyffcglwggbqvsethrsibkgovvobcrofqvludyqjfrzalfvuzndazjrvhfylxospjfjmebxjsxlfegadvfgvqxszcqkbffsqkdfoeczybkggqglonrjdobdtrpwywrphuwxbyxbahhiaptocnxidanwrevsbmhkidhjdenfounqmjeqwdyzdnywutovhxhpcobgvoljkbzwkfnginhndflxaauhxbzcpaikqtvcwuzgbooldwygbkdemxllyknqmvacryhpsgwwwmhziiimslqglbrlohbaecfvamnuujssvatgibscpiialblbinenrlktxxptiilgkgmuigwxqgzbhkfszjfsurntrfoznbfzhttpzropxntgayazhhudzhwsmkrblzcssvksoyhnoawoywphgjkftixhuqlhpnailmczmjpamlomjewppgwkrvulmfvdsxnfjphvbwwnhmbssxikgeuxaokmvfrqcfvnucjvahkjtocmlkyrqsqqjdeekwupbscxunvvwhgqviehucalwtbfyimiegzhyeevtbsqjyiejoldsooojswhciriqrprvvoqxiggiomreaxwonlxhjgjtxrjoiclgscfaknjbzcfzbcppnmwwsirszcgkfuqzwvciiljjppjrryienechmtzoviaccqeangixtsiijrbasjghqkocdqsaysfckjezpoyighspyursdxzthqymgspgnukxfozwcxelewcfsuxyrztbptnvmcdzynydbxzdvfqbetgyngwgfshulvrxzuyyjxdkufprkitqbzpofnumfeirzzqyvpyemcqijiavqtmrudhcqdowhxpiyfjwuhailttudtstoemkjvmzadxkcmsasbymlzxyuqvxlnsbtelcbybbbzldlgfdjeswfrvbhqyufsvyygazedahcomqwuvfapchgziprilwaguynwztzbdeprwnlttljxurwcjpmulmbhmqfllgnokegistclfnkzeienxqikflrrbwdocsdpwlzoebblonnvvrisjscodvigtnvwfandlourqxdglsdglobugflmbvuuirsprhsewowombuxtadeogawmnknifjqychsjcwhquvexsbqshwgnzebmpovwynucvmnzlvpfqwfixxcguiuvpvhemeamswopjdouyfbrbgbbgehaodvdbehnjjbbgrsruinvpomtxnudtdfihcnigxxrgyuormflusgmjsfiiznbcullwzveyswgsqvjfcxbxdngysqitfjyzxjxyfdwzzcuszdxcaabgohegzmcexafwlcuqfsshxmbyracuadaokgxluzptzuqkymdgfxnejqccqfwqiyhvgegadyueukqvyvbduqhdgmiyreobfvwlbfmgdimzufusavwvlfattirkpimufkhhptnudauxfoqhmoezvhtprmbgupccakjrfymjaighyypkovkkcfbwtccqshsurdlybzhchqjiqasfyepclqyfudxokpidswbvxlxhdjptlhyjopmzhmgcpdszubeozikwtjdyssrecspqhdrpqatfflhaolqptamomrmgmgkoycghfxyvztdfhkhxxxntabhmswseefuehaloamkzfngmznkwlzpnazzsxtzdavhjwuyygkzmzgaytmwglotlpugoqhrqcycauaabmapnirndejkrzfdoclcustkwtoxqqzrcziphbcnfoxxneccingchapdvdcluceydoonqsaxgzuwfyaolgquifaelcrfgydkmtzeozcwyysdxstkbkfjrhpcjhjshpetkdayccxcaphzkdklnrugymjjtudajhvukvuozrsajcbtfngugcagolsjgvlrdhlpeigezygiahdhxlbdqekgpcqxxbpckcupkavmydwbkckjnmnfqxmhbefyhwdsyxjlxgxxjvavxlfnzssrrgyskfsubvmcuxntdmrojrjheowdiquzxvtjamdejrgeovxtjqhsktzohvusoqrlnlwqzauiraoixodgenyogafpxbhltzyhmvxlvtvovkysycaepyvxaamydulyvkfhfeucxpssbrmzvmemnzjnbvngpzemlmtqspuqhmkifzkalqmyrvmutzciaivluqdnixfpmrzrqlucdicugqqzqsjsbeexxjmhhryvlxoblifotilzydyqyhlzorynalujeseprvtcdytyigxjjxzhhmivdhkesenywuoppjsuhntstsbeqcmxpwusdeyxkoyiimxzvpveeoyxjzezeqytosnuymrkapskdplahghlxflghpflhfgvztpxhjhjyzteqegxnnjktuqcjvnscvnbodayohhoibsyhzyuohejduloragvvtwkywkmfrbpsvqcwowlvduazgotguocnloohycprdekbuoximifrdfrjtkrpavfnltxlvmdbqpcndzvpidhnkayempvmnaaytxkrlnsbcwohvmwfpfszhqftibivbitxhfossivwemdbychphbqrsykabsxccqblwrfqzbnfpqjpuqeetwvlufnxakccddobvvrwygenznctfixyfsmbabzambcrgssdqlcosgcrvekcpkawcozcqycebhvkbpnrarguzkluqywfizbknbpfbtjfcgrgxgxayfuxrguigqporrahurmxlyepgvvgcvgaaazuitcomredkhkeyzejxibfewlirrkuujoedsvrjzuwghcfggqfprkvqydhpndlyrqdlluxmrtvyvagesnvmzqcxvlpkpaiismufitszmnxjpfnhskvscxpxlejahskzggfozzolmnxbvmknxifzhxzsdiumcfmiltzlunygcxjxkvnhdsinrhfvsahuhvdsqcfkrgsvddtpbgygahtuqzpibydiwgcokkzdstyxztnablgcscylbntenwmjeqaqaztsusqvldvnqerlgpwjepnrobdsrdjueemawewkjtxazqlhhhqlwfemijfcoqwuukxtptdyocyoulvbsoorvsdeekgucepxomsdhvexzeltqhwkxkbsehwitedwiuvzincrkiojncedlanimraqazbtfgpqakpkxtdjcrspvyugajomardcsewxknpmyewxybhasbrqclwcunpxguzyyvxkjnwjtugrvptptkfvvexqronxioximwsvjogdkowhgqxzceuyitqbkfystxbfuvcfkkkwzhefzdgdhabqvtrhysaurdblygtkqdhrmnynqerxgupeojlodlkuqogrubbmekgrxegnlxnrscvinjwqwjlnxtetuhfasnrpsyffxswpwuzkfycbhnqeiuxeeefwsynmystwmrnlnnvslzusnkyxhxcldjjvhwjircedutojglctlwnainzrkdeomnlwmxedbkixdzhmmjhzhxbrkbjvenltdyrpvxuxhcumddaqmkrthtnruwoalzvoamfvlzuuerhjujbhttcampsingkzigpiuxfiwaccrjmlvnuoizpuojecrpdbxultrrbqteumngxkwuzetqbjzfnququtnfnewowpsrbizbsxxrcqjdziknbhfvasanzzexqwougqvznssrkcwlmhanogkqangbmkzcgpwphtqvnkmxojlbslqitdyuqexcoygxofovyesmohldsygkkwsdzszrxzvnxcmnhalhgdtvkhacfgoregxgzyxyxtnvxciectnlzjglqioxqcrulqcmoammvzjudtagpntowbbojpozufvhvytlahxxiirmcrutgnjdokrxchyymtfjravrhuopfhbjyxchklkyxdxzlvxzpcjiegclcsdhagqaeshofrpdxmcikcjbgsjlalwdebkgibgmvocbhrggekoomyptsaevocyuekaoliajyckgwqmaadqpdhixjosxsqrydtmocozarjinbxpechtfodcztxxnpqmskyjmnioguxvvwmbytwfjbjiugfiwywqiuzwjikpcjmzhybftxmezwnvcufasbrcysyhalzewneeohjhgwmhubdwvkzqossmktvnewrakxeygqhnotuiuzgskhkyzcmmvjzbgsesskqyaxlqtgapfjjrqtrsyfgvpfxvzbprlfqoedgzjhrrsaikwacufipwpmtrpiidparwezvpimgaprlltnfayuxpjqgabrdqtwmzwkpewxfnqqajffkfcjxnbfncyrtspftlpiqoixdypekwluepdbceisjhjcbyjumbferpbunsaxomtubyvgfeyonhqohbivcpzvecquuqrlenfildoqjmewvwmeawacmzyqcqkyielnrtxewlvfxbdsapyalyezyescuecfioubhrifcdmbgpvigtirsptstlwqpyvyorbvijcmoonxfifldqfxfypyjloymlyaccwmlyycplzuvggbylydloeubuungvokxmxkmvmbjnwgwehurgycueyxyulgpbrmnqxznldwzbdvfmpyspcotamuuzamatynjxoxjrvisafznwxfozujbidyhekhziwlgkkrefbwigwvevcsvycwgfupleynpuyxhionppjxxhsbdvwatywcfrrtxqgomelvobidsudrdxtisriopfswyjpxbxmqdzlrdwxxqapvxkesbmiqtaorlgrpddfhesyjqxhixwexgiphwzzqbnhotydzdkgkfgtveaedwiaesrloqmetcoixolwuycedlxypyeswmvbgmoxfddyfrgciubcsdgxqdvfdcaaovdxhtuowxndrvizrjblojifmgkqiksyhxxpstfprsukqcjjlmvavffjnrbxevylsvcnpicicwsubdemrbmogtxwnbtrwrernheerimvggshjwucziqhepdrqxinqmefvkjosvmydegmacqbmgiqwmhmlrbbgfhdpssjoeitkqgmsyngfvxdheruwtwcaffsxzbnfjhpbpbvnocumzxvfpqdiohktpcsoegwppnrerotfqqtrnpxefcotkzozbgphonxdbqjsefzvvtmkilppofiaeybieqptgmyhckbhpaekvswfgluwrewxcxfjpvexjceomhxdkbpfvmnbxhxqovosuvbmsfjckqsyxpchsrnndardjovzmlsghvszbednuvlrknzchosmqjpbznblytufqmhtskgmiseshfxotpdlyumxhnlgifnztuumfbynvehcjgtevwpvqcvarggcltbgoxsvytktxtyhatnvrdtjhojyurchldnbbgybzixybxfdqvbjyushiehevklipajsihujrtivqpyikzrktlrdrzhnjuxyvhrdqlnievdwmdexfvhyizeaylpjimhdvyimlvwrsbnferejonkzmqzmbqvledoadxopukgpnuwrnadenpdcfeoiumuarkcujqlecstporjdrohgfkimozwknslednyogkskenauelxxbfegrosgposchdgmthabtvlzkntrysozxuhplzxaqpfzvlnounrpkcovqhmqacszzzqkbnmtfruafhqzwhphlfcbnqupsoqtphdswqldjfdoovqlehuqmytbonqibhctqhlmzxsjevzvtpgxycnlajoowfyaoatgiguhdmskkshdhpcirqtrbjfxofzegumqbhzgtssfkzitolbfdwwegddwjfdrzphcyijuabzmdigrvjxaivgqbloksrdsjmwhufbvjbjmlrfideklasdbfrnylssweodywhvfkhtxyyhbftoflriqjxqwpisvxxvtgtasavpyvyaarofcipvtmlpdwjytiwoppqjplzngzpjrgqvogsjugaacjaxrwlilbsaotqwshflpwhfcboyhoylzzitvvbjyvjmobjjlowamfgohwnqlnckmmdkihtgcevtigetwatjgbxnymdlchxoudyektmoyhjgpnzmouvuyujyjojlwgzslawvtimtsvzhjatzxqtvletusehqmiiykevgphzhfbqobkpyakvnoqjgwqzjbhjloerformtsejvoywritgwkqegidrlnaxbfqgvhuobyzzpxvifoqdaijhrnaecbbdisldbhtfhseypbiwpzbqhkzazzfbcigkatpeaijkcnirorpfsqxzdyccahecpmpsgewiphsrwdlmwcrovrpypraryguqtlkbrgjgpealhnxdpqtkjikbansytoqozaptibzxfbimqhrgaksjsfkssdtnrjctmtmuunsbrcnhmgpmqixlpifhnyuekyzwsnsobkqupfbbmrpebmpqwvxjvtohspdmdwcgisazadcouruvgmncjkmegcmytrmwpoeajezliczevtcdfpgocuviwjipauoskusvzrgjvhprdrwihczjywtwfbohxczjwrfxlnigvazyrwiaajlbfexmhlwgpvqopxnckykhymfrkqskzdnhklttypaqnseeptibrsjreqjogdbggonsbimaamqpgwvvpdwjvhccylqeotmxibplkdnmrfbxbwutbrewygyysrdikpfurxgdavpubsrcqmxrfbpfioechhmrysoprwstrjnsbhxtvukcyahiqnkxuyqvqekjafdsqsmubjnweaycagmsvyrswhnnozyqedkxwxrxgewmeuqgccyyarqxbdmpekhlosimpzlxfhkkccseftefkwelzqcedkrtezftyqsfycrcfkimdntpjydlqhrtriovjtqhmjomngquqyivncmzapmsxdoqncowygfmrtyhzobrokmcobbqqnipswihzydzgklyfjffziynulrkouaehjwbfgigenfmzskfbrmccksyxjjlelsnuopcwzkcpsookbtoshqwskxpuidatvnoleshgcjvuxlhahvtolrgyoysybusyjijqaswedtbceidldycqpiogiiejcyjmgucimanptoszyvnbtptkziqisxtxvdjexnmkpzbiptjnqwqjnkwnumvololhtulrjzdyzeiqaugsswegiateoqtaeejybwrkvulwavncpvvirzoczjgnzzpfgyfhuwtsseovcdxryubstpuuackzezhkamrwlkodrdatgamhuozqdtkgvufbwolwbcumpjriosbwsndmbcchvpptlwwjlihmmcablrjzlm")
