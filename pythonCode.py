#!/usr/bin/env python3
import psycopg2

DBName = "news"


mostPopularThreeArticles = """
                            SELECT articles.title as Title, COUNT(log.path) AS
                            ViewCounter
                            FROM articles, log
                            WHERE SUBSTRING(log.path, 10) = articles.slug
                            GROUP BY Title
                            ORDER BY (ViewCounter) DESC
                            LIMIT 3;
                           """
mostPopularArticleAuthors = """
                            SELECT authors.name as AuthorName, COUNT(log.path)
                            AS ArticleCounter
                            FROM authors , articles , log
                            WHERE authors.id = articles.author
                            AND SUBSTRING(log.path,10) = articles.slug
                            GROUP BY AuthorName
                            ORDER BY (ArticleCounter) DESC;
                           """
requestsLeadToErrors = """
                        SELECT date , errorPrecentage
                        FROM (
                        SELECT error.date AS date,
                         error.notOK::DOUBLE PRECISION
                        /request.all::DOUBLE PRECISION*100 AS errorPrecentage
                        FROM  (SELECT time::DATE AS date, COUNT(time) AS notOK
                        FROM log
                        WHERE status NOT LIKE '%OK'
                        GROUP BY date ) AS error
                        JOIN (SELECT time::DATE AS date, COUNT(time) AS all
                        FROM log
                        GROUP BY date) AS request
                        ON error.date = request.date ) AS presentageCalculate
                        WHERE errorPrecentage > 1;
                       """


def DBConnection(query):
        """database connection and excution and result """
        db = psycopg2.connect(database=DBName)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result


def printMostPopularThreeArticles(result1):
    print("What are the most popular three articles of all time?")
    for Title, ViewCounter in result1:
        print("\"{}\" _ {} views".format(Title, ViewCounter))


def printMostPopularArticleAuthors(result2):
    print("Who are the most popular article authors of all time?")
    for AuthorName, ArticleCounter in result2:
        print("{} _ {} views".format(AuthorName, ArticleCounter))


def printRequestsLeadToErrors(result3):
    print("On which days did more than 1% of requests lead to errors?")
    for date, errorPrecentage in result3:
        print("{0:%B %d, %Y} _ {1:.1f} % errors".format
              (date, round(errorPrecentage, 1)))


def main():
        result1 = DBConnection(mostPopularThreeArticles)
        printMostPopularThreeArticles(result1)
        result2 = DBConnection(mostPopularArticleAuthors)
        printMostPopularArticleAuthors(result2)
        result3 = DBConnection(requestsLeadToErrors)
        printRequestsLeadToErrors(result3)


if __name__ == '__main__':
    main()
