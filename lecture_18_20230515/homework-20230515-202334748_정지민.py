# 객체를 만들어보자
# class 작성 후
# class 내부에서 사용될 함수 정의
# 이때 정의는 private과 public 변수 모두 사용
# 시험에 낸다고 하심
from datetime import timedelta, timezone, date
from typing import TypeVar, Tuple, List, Union, Callable, Optional

timezone(timedelta(hours=9))

class SNS:
    def __init__(self, type, id, name, description, url):
        self.__type = type
        self.id = id
        self.name = name
        self.description = description
        self.url = url

    def toString(self):
        result = "[" + self.__type + "] " + self.name + " @" + self.id + " (" + self.description + ") - " + self.url
        return result

class BelongTo:
    def __init__(self, type, department, name, description, position, start_date: date, is_end = False, end_date: Union[date, None] = None):
        self.__type = type
        self.department = department
        self.name = name
        self.description = description
        self.position = position
        self.__start_date = start_date
        self.is_end = is_end
        self.end_date = end_date

    def toString(self):
        result = "[" + self.__type + "] " + self.name + " " + self.department + ", " + self.position + " (" + self.__start_date.strftime('%Y-%m-%d') + " ~ " 
        if (self.is_end):
            result +=  self.end_date.strftime('%Y-%m-%d') + ") "
        else:
            result += "현재) "

        result += self.description
        return result


class ClubInfo:

    def __init__(self, type, belong_to, category, name, description, position, start_date: date, is_end = False, end_date: Union[date, None] = None):
        self.__type = type
        self.__belong_to = belong_to
        self.__category = category
        self.name = name
        self.description = description
        self.position = position
        self.__start_date = start_date
        self.is_end = is_end
        self.end_date = end_date

    def toString(self):
        result = "[" + self.__type + "] " + self.__belong_to + " " + self.__category + " 동아리 - " + self.name + ", " + self.position + " (" + self.__start_date.strftime('%Y-%m-%d') + " ~ " 
        if (self.is_end):
            result +=  self.end_date.strftime('%Y-%m-%d') + ") "
        else:
            result += "현재) "

        result += self.description
        return result

class LifeCareer:
    LIFE_CAREER_TYPE_STUDENT_COUNCIL = "학생회"
    LIFE_CAREER_TYPE_CLUB = "동아리"
    LIFE_CAREER_TYPE_TEAM = "팀"
    LIFE_CAREER_TYPE_PERSONEL = "개인"
    LIFE_CAREER_TYPE_OTHER = "그외"

    def __init__(self, type, name, description, position, start_date: date, is_end = False, end_date: Union[date, None] = None):
        self.__type = type
        self.name = name
        self.description = description
        self.position = position
        self.__start_date = start_date
        self.is_end = is_end
        self.end_date = end_date

    def toString(self):
        result = "[" + self.__type + "] " + self.name + ", " + self.position + " (" + self.__start_date.strftime('%Y-%m-%d') + " ~ " 
        if (self.is_end):
            result +=  self.end_date.strftime('%Y-%m-%d') + ") "
        else:
            result += "진행중) "

        result += self.description
        return result
        

class ProjectInfo:
    PROJECT_TYPE_STUDENT_COUNCIL = "학생회"
    PROJECT_TYPE_CLUB = "동아리"
    PROJECT_TYPE_COMPETITION = "대회"
    PROJECT_TYPE_OTHER = "그외"
    PROJECT_TYPE_PERSONAL = "개인"

    PROJECT_TEAM_TYPE_PERSONAL = "개인"
    PROJECT_TEAM_TYPE_TEAM = "팀"

    PROJECT_TECH_TYPE_MOBILE_APP = "앱"
    PROJECT_TECH_TYPE_WEB = "웹"
    PROJECT_TECH_TYPE_HARDWERE = "하드웨어"
    PROJECT_TECH_TYPE_SYSTEAM = "시스템(종합)"

    def __init__(self, type, team_type, tech_type, name, description, position, start_date: date, is_end = False, end_date: Union[date, None] = None):
        self.__type = type
        self.team_type = team_type
        self.tech_type = tech_type
        self.name = name
        self.description = description
        self.position = position
        self.__start_date = start_date
        self.is_end = is_end
        self.end_date = end_date

    def toString(self):
        result = "[" + self.__type + " / " + self.team_type + " / " + self.tech_type + "] " + self.name + ", " + self.position + " (" + self.__start_date.strftime('%Y-%m') + " ~ " 
        if (self.is_end):
            result +=  self.end_date.strftime('%Y-%m') + ") "
        else:
            result += "진행중) "

        result += self.description
        return result


class Jimin0629:
    def __init__(self):
        self.__name = "정지민"               # 이름
        self.__gender = "남성"
        self.__birth = date(2004, 6, 29)    # 생일
        self.__mbti = "INFP" # 평균적 MBTI
        self.mbti = "INFP" # 현재 MBTI
        self.__nickname = "DotJM" # 닉네임
        self.__sns = [SNS("Instagram", "dotjm.jm", "DotJM 지민", "개발인스타그램", "https://www.instagram.com/dotjm.jm"), SNS("Github", "dotjm", "정지민(Jeong Jimin)(DotJM)", "", "https://www.github.com/dotjm")]
        self.__location = "기숙사" # 현재위치
        self.__belong_to = [BelongTo("대학교", "컴퓨터공학부(컴퓨터공학전공)", "가천대학교", "", "학부생", date(2023, 3, 1), False)]                       #소속
        self.__club = [ClubInfo("교내", "가천대학교", "정보보호", "Pay1oad", "", "동아리원", date(2023, 3, 8)), ClubInfo("교내 중앙동아리", "가천대학교", "작사작곡", "소리상자", "", "동아리원", date(2023, 3, 10))]  # 동아리
        self.__life_career = [LifeCareer(LifeCareer.LIFE_CAREER_TYPE_STUDENT_COUNCIL, "삼괴고등학교 2020-21학년도 학생회 창의경영부", "", "차장", date(2020, 10, 2), True, date(2021, 8, 10)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_CLUB, "삼괴고등학교 창의공학동아리 뉴턴(NewTurn)", "", "회장", date(2021, 3, 10), True, date(2022, 3, 16)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_TEAM, "HELTY SOLUTIONS(헬티 솔루션즈) 팀", "", "팀장", date(2021, 8, 19), True, date(2022, 11, 25)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_STUDENT_COUNCIL, "삼괴고등학교 2021-22학년도 학생회 창의경영부", "", "부장", date(2021, 9, 14), True, date(2022, 7, 7)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_CLUB, "삼괴고등학교 창의공학동아리 뉴턴 소프트웨어(NewTurn SW)", "", "회장", date(2022, 3, 16), True, date(2023, 6, 22)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_STUDENT_COUNCIL, "삼괴고등학교 선거관리위원회", "", "위원", date(2022, 7, 4), True, date(2022, 7, 8)), LifeCareer(LifeCareer.LIFE_CAREER_TYPE_PERSONEL, "DotJM Studio", "", "팀장", date(2021, 4, 5)), ]
        self.__projects = [ProjectInfo(ProjectInfo.PROJECT_TYPE_PERSONAL, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_MOBILE_APP, "비공식 중학교 앱 개발 및 운영", "", "해당없음", date(2018, 5, 1), True, date(2020, 2, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_PERSONAL, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_WEB, "학교생활정보 사이트 StuLife 개발 및 운영", "", "팀장", date(2020, 3, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_COMPETITION, ProjectInfo.PROJECT_TEAM_TYPE_TEAM, ProjectInfo.PROJECT_TECH_TYPE_SYSTEAM, "'HELTY SYSTEM - 무인 QR 체크인 게이트' 개발", "", "팀장", date(2021, 8, 1), True, date(2021, 11, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_OTHER, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_WEB, "'SIS Page - 온라인 서명 시스템' 개발", "", "개발자", date(2021, 12, 1), True, date(2021, 12, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_CLUB, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_SYSTEAM, "'NewTurn Intranet - 동아리 인트라넷' 개발", "", "회장", date(2021, 12, 1), True, date(2022, 5, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_CLUB, ProjectInfo.PROJECT_TEAM_TYPE_TEAM, ProjectInfo.PROJECT_TECH_TYPE_SYSTEAM, "Project.SID - 안전한 모바일 학생증 프로젝트", "", "팀장", date(2022, 5, 1), True, date(2022, 7, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_STUDENT_COUNCIL, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_SYSTEAM, "고등학교내 선거관리위원회 개표 프로그램 개발", "", "해당없음", date(2022, 7, 1), True, date(2022, 7, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_PERSONAL, ProjectInfo.PROJECT_TEAM_TYPE_PERSONAL, ProjectInfo.PROJECT_TECH_TYPE_WEB, "행사용 퀴즈 버저 개발", "", "해당없음", date(2022, 7, 1), True, date(2022, 7, 1)), ProjectInfo(ProjectInfo.PROJECT_TYPE_OTHER, ProjectInfo.PROJECT_TEAM_TYPE_TEAM, ProjectInfo.PROJECT_TECH_TYPE_SYSTEAM, "행사 참여자 관리 프로그램 개발", "", "개발책임자", date(2023, 3, 1))]


    def printAllInfo(self):
        print("===== 정보 출력 =====")
        print()
        print("이름:", self.__name)
        print("닉네임:", self.__nickname)
        print("성별:", self.__gender)
        print("생일:", self.__birth.strftime('%Y-%m-%d'))
        print("평균적인 MBTI:", self.__mbti)
        print("현재 MBTI:", self.mbti)
        print("SNS 목록 : ")
        for sns in self.__sns:
            print(" - ", sns.toString())

        print("현재 위치 :", self.__location)
        
        print("소속 목록 : ")
        for belong_to in self.__belong_to:
            print(" - ", belong_to.toString())
        print("동아리 목록 : ")
        for club in self.__club:
            print(" - ", club.toString())
        
        print("--- 소속 경력 ---")
        for life_career in self.__life_career:
            print(" - ", life_career.toString())
        print("-----------")
        print("--- 프로젝트 목록 ---")
        for project in self.__projects:
            print(" - ", project.toString())
        print("-----------")


        print()
        print("=====================")


    def getName(self):
        return self.__name
    
    def reName(self, name):
        self.__name = name

    def getGender(self):
        return self.__gender
    
    def getBirth(self):
        return self.__birth

    def getBirthText(self):
        return self.__birth.strftime('%Y-%m-%d')

    def getMBTI(self):
        return self.__mbti
    
    def setMBTI(self, mbti):
        self.__mbti = mbti
    
    def getNickname(self):
        return self.__nickname
    
    def setNickname(self, nickname):
        self.__nickname = nickname

    def getSNS(self):
        return self.__sns
    
    def getSNSText(self):
        result = ""
        for sns in self.__sns:
            result += sns.toString()
            result += "\n"
        return result
    
    def addSNS(self, new_sns: SNS):
        self.__sns.append(new_sns)

    def getLocation(self):
        return self.__location
    
    def setLocation(self, location):
        self.__location = location

    def getBelongTo(self):
        return self.__belong_to
    
    def getBelongToText(self):
        result = ""
        for belong_to in self.__belong_to:
            result += belong_to.toString()
            result += "\n"
        return result
    
    def addBelongTo(self, new_belong_to: BelongTo):
        self.__belong_to.append(new_belong_to)

    def getClub(self):
        return self.__club
    
    def getClubText(self):
        result = ""
        for club in self.__club:
            result += club.toString()
            result += "\n"
        return result
    
    def addClub(self, club: ClubInfo):
        self.__club.append(club)

    def getLifeCareer(self):
        return self.__life_career
    
    def getLifeCareerText(self):
        result = ""
        for life_career in self.__life_career:
            result += life_career.toString()
            result += "\n"
        return result
    
    def addLifeCareer(self, life_career: LifeCareer):
        self.__life_career.append(life_career)

    def getProjects(self):
        return self.__projects
    
    def getProjectsText(self):
        result = ""
        for project in self.__projects:
            result += project.toString()
            result += "\n"
        return result
    
    def addProjects(self, project: ProjectInfo):
        self.__projects.append(project)


print("JeongJimin Info v1.0 (2023-05-28)")
print("")
print("정지민 정보 조회 시스템에 접속하신 것을 환영합니다!")
print("=== 상태 ===")
print("언어 : 한국어")
print("조회 권한 : 전부")
print("설정 권한 : 일부")
print("============")
jimin = Jimin0629()
# print(jimin.getName())
jimin.printAllInfo()


while True:
    print("=== 명령어 목록 ===")
    print("1. 특정 정보 가져오기")
    print("2. 특정 정보 변경하기")
    print("3. 전체 정보 출력")
    print("4. 종료")
    print("==================")
    in_val = int(input("번호 입력 : "))

    if (in_val == 1):
        print("=== 정보 종류 ===")
        print("1. 이름")
        print("2. 성별")
        print("3. 생일")
        print("4. 평균 MBTI")
        print("5. 현재 MBTI")
        print("6. 닉네임")
        print("7. SNS 목록")
        print("8. 현재 위치")
        print("9. 소속 목록")
        print("10. 소속 동아리 목록")
        print("11. 경력 목록")
        print("12. 프로젝트 목록")
        print("13. 취소하기")
        print("==================")
        in_val_2 = int(input("번호 입력 : "))
        
        if (in_val_2 == 1):
            print("이름 :", jimin.getName())
        elif (in_val_2 == 2):
            print("성별 :", jimin.getGender())
        elif (in_val_2 == 3):
            print("생일 :", jimin.getBirthText())
        elif (in_val_2 == 4):
            print("MBTI :", jimin.getMBTI())
        elif (in_val_2 == 5):
            print("MBTI :", jimin.mbti)
        elif (in_val_2 == 6):
            print("닉네임 :", jimin.getNickname())
        elif (in_val_2 == 7):
            print("SNS 목록 :", jimin.getSNSText())
        elif (in_val_2 == 8):
            print("현재 위치 :", jimin.getLocation())
        elif (in_val_2 == 9):
            print("소속 목록 :", jimin.getBelongToText())
        elif (in_val_2 == 10):
            print("소속 동아리 :", jimin.getClubText())
        elif (in_val_2 == 11):
            print("경력 :", jimin.getLifeCareerText())
        elif (in_val_2 == 12):
            print("프로젝트 목록 :", jimin.getProjectsText())
        elif (in_val_2 == 13):
            print("종료합니다. ")
            break
        else:
            print("없는 명령어입니다. ")
    elif (in_val == 2):
        print("=== 정보 종류 ===")
        print("1. 이름")
        print("2. 성별")
        print("3. 생일")
        print("4. 평균 MBTI")
        print("5. 현재 MBTI")
        print("6. 닉네임")
        print("7. SNS 목록")
        print("8. 현재 위치")
        print("9. 소속 목록")
        print("10. 소속 동아리 목록")
        print("11. 경력 목록")
        print("12. 프로젝트 목록")
        print("13. 취소하기")
        print("==================")
        in_val_2 = int(input("번호 입력 : "))
        
        if (in_val_2 == 1):
            in_val_3 = input("변경할 이름 입력 : ")
            jimin.reName(in_val_3)
        elif (in_val_2 == 2):
            print("변경 권한 없음")
        elif (in_val_2 == 3):
            print("변경 권한 없음")
        elif (in_val_2 == 4):
            print("변경 권한 없음")
        elif (in_val_2 == 5):
            in_val_3 = input("변경할 MBTI 입력 : ")
            jimin.mbti = in_val_3
        elif (in_val_2 == 6):
            in_val_3 = input("변경할 닉네임 입력 : ")
            jimin.setNickname(in_val_3)
        elif (in_val_2 == 7):
            type = input("SNS 종류 (Instagram 등)을 입력 : ")
            id = input("SNS ID를 입력 : ")
            name = input("SNS 닉네임을 입력 : ")
            description = input("설명을 입력 : ")
            url = input("SNS 주소를 입력 : ")

            jimin.addSNS(SNS(type, id, name, description, url))
            print("추가 완료")
        elif (in_val_2 == 8):
            in_val_3 = input("이동시킬 위치 입력 : ")
            jimin.setLocation(in_val_3)
        elif (in_val_2 == 9):
            print("권한 없음")
            # print(jimin.getBelongToText())
        elif (in_val_2 == 10):
            print("권한 없음")
            # print(jimin.getClubText())
        elif (in_val_2 == 11):
            print("권한 없음")
            # print(jimin.getLifeCareerText())
        elif (in_val_2 == 12):
            print("권한 없음")
            # print(jimin.getProjectsText())
        elif (in_val_2 == 13):
            print("종료합니다. ")
            break
        else:
            print("없는 명령어입니다. ")
    elif (in_val == 3):
        jimin.printAllInfo()
    elif (in_val == 4):
        print("종료합니다. ")
        break
    else:
        print("없는 명령어입니다. ")

print("이용해주셔서 감사합니다. (입력한 정보는 저장되지 않습니다)")
