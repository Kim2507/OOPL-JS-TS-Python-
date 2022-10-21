/*Author: My Kim Trinh 
CSC237 OOPL : TypeScript classes and inheritance demonstration
*/


/*Enumeration type for NewsCategory*/
enum NewsCategory { BUSINESS = 0, POLITICS, TECH, ENTERTAINMENT, SPORTS };

/*Abstract Publisher class(subclasses will be NYT,CNN,BBC)*/
abstract class Publisher {

    abstract attach(sub: Subscriber): void

    abstract detach(sub: Subscriber): void
}


/*Subclass NewYorkTimeBreakingNews of Publisher class*/
class NewYorkTimesBreakingNews extends Publisher {

    private subscribers: Subscriber[] = [];

    attach(sub: Subscriber) {

        if (!this.subscribers.includes(sub))
        this.subscribers.push(sub);
        console.log("Now have " + this.subscribers.length + " subscribers.\n");
    }

    detach(sub: Subscriber) {
        if (this.subscribers.includes(sub)) {
            this.subscribers.splice(this.subscribers.indexOf(sub), 1);
            console.log("Now have " + this.subscribers.length + " subscribers.\n");
        }
        else throw new Error("This subcriber is not included in pulisher.\n");
    }
    /*Checking valid argument and assigned to class instance variable*/

    publishNewsItem(newsCategory: NewsCategory, newsTitle: string): void {
        for (let sub of this.subscribers) {
            sub.breakingNews(newsCategory, newsTitle);
        }
    }

}

/*A Subscriber interface with one method:
breakingNews(newsCategory: NewsCategory, newsTitle: string): void;*/
interface Subscriber {

    breakingNews(newsCategory: NewsCategory, newsTitle: string): void;
}

/*BusinessNewsSubcriber class (subclass of Subscriber)*/
class BusinessNewsSubscriber implements Subscriber {

    breakingNews(newsCategory: NewsCategory, newsTitle: string) {
        if ((newsCategory == NewsCategory.BUSINESS) && (newsTitle != "")) {
            console.log(NewsCategory[newsCategory] + " :" + newsTitle + "\n");
        }
        else console.log("This is not Business news");
    }
}

/*PoliticsSubcriber class (subclass of Subscriber)*/
class PoliticsNewsSubscriber implements Subscriber {

    breakingNews(newsCategory: NewsCategory, newsTitle: string) {
        if (newsCategory == NewsCategory.POLITICS && (newsTitle != "")) {
            console.log(NewsCategory[newsCategory] + ":" + newsTitle + "\n");
        }
        else console.log("This is not Politics news");
    }
}

/*KeyWordSubcriber class (subclass of Subscriber)*/
class KeyWordSubscriber implements Subscriber {

    keyword: string = "";
    constructor(key: string) {
        this.keyword_check(key);
    }
    keyword_check(key: string) {
        if (key != "") this.keyword = key;
        else console.log("empty keyword...Pls enter something...\n");
    }
    breakingNews(newsCategory: NewsCategory, newsTitle: string) {

        console.log(this.keyword);
        console.log(newsTitle.toLowerCase());
        if (newsTitle.toLowerCase().includes(this.keyword)) {
            console.log("KEYWORD [" + this.keyword + "]" + ":" + newsTitle + "\n");
        }
        else console.log("Sorry,no news match this key word.\n");
    }
}

console.log("\t----------\n");

let nyt = new NewYorkTimesBreakingNews();

/*Creating 3 subscribers and attach it to NYT*/
let business_sub = new BusinessNewsSubscriber();
nyt.attach(business_sub);

let polictics_sub = new PoliticsNewsSubscriber();
nyt.attach(polictics_sub);

let keyword_sub = new KeyWordSubscriber('biden');
nyt.attach(keyword_sub)

/*Publishing news*/
nyt.publishNewsItem(NewsCategory.BUSINESS, "J&J plans to split into two companies.");
nyt.publishNewsItem(NewsCategory.POLITICS, "Biden and Xi to Hold Virtual Summit.");






