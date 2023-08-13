from requests_html import HTMLSession
import json

def scrap(year):
    session = HTMLSession()
    total_data = []
    
    start = 1
    
    while start < 1000:
        data = []

        url = f"https://www.imdb.com/search/title/?title_type=feature&year={year}&start={start}"

        response = session.get(url)

        movieWrapperList = response.html.find(".lister-item-content")

        for movieWrapper in movieWrapperList:
            movieName = movieWrapper.find(".lister-item-header a", first=True).text
            movieYear = movieWrapper.find(".lister-item-year", first=True).text
            movieLink = movieWrapper.find(".lister-item-header a", first=True).attrs["href"]

            try:
                movieCertificate = movieWrapper.find(".certificate", first=True).text
            except AttributeError:
                movieCertificate = "N/A"

            try:
                movieTime = movieWrapper.find(".runtime", first=True).text
            except AttributeError:
                movieTime = "N/A"

            try:
                movieGenre = movieWrapper.find(".genre", first=True).text
            except AttributeError:
                movieGenre = "N/A"

            try:
                movieRating = movieWrapper.find("strong", first=True).text
            except:
                movieRating = "N/A"

            p_D_tags = movieWrapper.find('p[class=""]')
            for p in p_D_tags:
                if "Director:" in p.text:
                    movieDirector = p.find("a", first=True).text
                    break
            else:
                movieDirector = "N/A"

            p_S_tags = movieWrapper.find('p[class=""] a')
            movieStarsList = [star.text for star in p_S_tags]
            movieStars = ",".join(movieStarsList)
            data.append({
                'movieName': movieName,
                'movieYear': movieYear,
                'movieCertificate': movieCertificate,
                'movieRating': movieRating,
                'movieTime': movieTime,
                'movieGenre': movieGenre,
                'movieDirector': movieDirector,
                'movieStars': movieStars,
                'movieLink': movieLink
            })
        total_data.extend(data)
        print(f"Year {year}, Start {start + 49} Done")

        start += 50

    return total_data

if __name__ == "__main__":
    years = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    merged_data = []
    for year in years:
        total_data = scrap(year)
        merged_data.extend(total_data)

    with open(f"Merged_Movies_data.json", 'w') as json_file:
        json.dump(merged_data, json_file, indent=2)
