/*A NewYorkTimesBreakingNews class, which extends Publisher.  
This class must include one method:
publishNewsItem(newsCategory: NewsCategory, newsTitle: string): void

A Subscriber interface with one method:
breakingNews(newsCategory: NewsCategory, newsTitle: string): void;

Three concrete subscribers.
BusinessNewsSubscriber that only prints out “business” news.
PoliticsNewsSubscriber that only prints out “politics” news.
KeyWordSubscriber that only prints out news that matches a keyword.  For example, if you initialize KeyWordSubscriber with “biden”, it will print out any news story that mentions Biden.

Here is a sample run of my code:

BUSINESS: J&J plans to split into two companies.
POLITICS:  Biden and Xi to Hold Virtual Summit.
KEYWORD [biden]  Biden and Xi to Hold Virtual Summit.
*/

//Enumeration type for NewsCategory
enum NewsCategory {BUSINESS, POLITICS, TECH, ENTERTAINMENT, SPORTS};

class Publisher{

    subscriber: string[]=[];

    constructor(subscriber:string){
        this.attach(subscriber);
    }


    //Declares a set of methods for managing subscribers.
    //abstractmethod
    attach(sub: string) {
        if(sub!="") this.subscriber.push(sub);
        else throw new Error("Invalid");
        //return this.subscriber;
    }

    detach(sub: string){
        if(this.subscriber.includes(sub)){
            this.subscriber.splice(this.subscriber.indexOf(sub),1);
        }
        else throw new Error("this subcriber is not included in pulisher...");
        
    }
}

/*A NewYorkTimesBreakingNews class, which extends Publisher.  
This class must include one method:
publishNewsItem(newsCategory: NewsCategory, newsTitle: string): void*/

class NewYorkTimesBreakingNews extends Publisher{
    //private newsCategory: NewsCategory[];
    private newsTitle: string;
    constructor(subscriber:string,newsCategory: NewsCategory, title:string){
        super(subscriber);
        this.publishNewsItem(newsCategory,title);

    }

    publishNewsItem(newsCategory: NewsCategory, newsTitle: string): void{
        if(newsTitle!="") this.newsTitle = newsTitle;
        //this.newsCategory = newsCategory;
    }
        

}

/*A Subscriber interface with one method:
breakingNews(newsCategory: NewsCategory, newsTitle: string): void;*/
interface Subcriber{
    
    breakingNews(newsCategory: NewsCategory, newsTitle: string): void;
}

/*Three concrete subscribers.
BusinessNewsSubscriber that only prints out “business” news.
PoliticsNewsSubscriber that only prints out “politics” news.
KeyWordSubscriber that only prints out news that matches a keyword.  
For example, if you initialize KeyWordSubscriber with “biden”, 
it will print out any news story that mentions Biden.
*/



let BusinessNewsSubscriber= new NewYorkTimesBreakingNews("Business",NewsCategory.BUSINESS,"Something");
console.log(BusinessNewsSubscriber);

//let BusinessNewsSubscriber = new NewYorkTimesBreakingNews("BUSINESS",)
/*BUSINESS: J&J plans to split into two companies.
POLITICS:  Biden and Xi to Hold Virtual Summit.
KEYWORD [biden]  Biden and Xi to Hold Virtual Summit.*/


