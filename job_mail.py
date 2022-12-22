# Cc: tommy.choi@generation.org, erica.ma@generation.org, leon.lai@generation.org

# Subject: Junior Data Engineer Application - Allen Kong - (Generation Graduate Job Application)


def jobmail(cfname, post, rece='Hiring Manager', jobboard = 'JobsDB'):
    cname = cfname

    mail = f'Dear {rece},\n\nI am applying for the position of {post} at {cfname} as advertised on the job board in {jobboard}.\
I recently finished Generation X CLAP@JC Junior Data Engineer Program. \
With my previous training of being a junior data engineer, I believe Datago is an ideal place to put my certifications to work using my strong technical skills and my commitment to working as a team to \
innovate and maintain.\n\nThe wide range of technological services and laser focus on the value of a dynamic, \
professional workplace that promotes a positive environment are admirable qualities of Datago. \
My previous working experience as a hardware engineer at E-Vision gave me the chance to work in pressure-filled \
situations related to issues. I had to build a physical network and security systems for the client within a limited \
period of time and learnt to work as a team to build a whole network system and design the pipeline. \
It was focused on the skills of quick-thinking, problem-solving, and how to cooperate with parties from different industries \
because there might be a worker who was an electrician or a plumber.\n\nI have spent the last several weeks in an \
incredible junior data engineer training program, which has improved my technical skills, behavioural skills, and \
mindsets to become a data engineer. During this time, I have had a wide range of exposure to the Python programming \
language, along with experience in SQL, Agile, GitHub, and Azure, powerBI  etc. that let me keep up to date of how the real \
world works. I also have had extensive practice problem solving, coding, and running tests and the opportunity to practice \
important skills such as communication, teamwork, growth mindset, personal responsibility, and persistence.\n\n\
Given that the {post} role at Datago is asked to competently address new challenges, react to changes in the \
business environment, manage priorities, and creatively suggest or build and maintain the existing code in order \
to increase performance, I strongly believe that my personality of teamwork, growth mindset and persistence makes me \
an ideal candidate for the position.\n\nI am excited by the opportunity to contribute to Datago as a {post}. I would \
like to develop my career path in Datago and grow with your team. I would welcome the opportunity to further discuss my \
qualifications for this position with you.\n\nSincerely,\n\nAllen Kong\n\nEnclosure: Resume'

    mail= mail.replace('Datago', cname)
    return mail


def writemail(mail):    
    ''' path = 'output.txt' '''

    path = '/Users/dev/Documents/cv/output.txt'
    with open(path, 'w') as f:
        f.write(mail)


def main():
    mail = jobmail('Mayer Brown', 'junior data engineer')
    writemail(mail)
    print('mail created successfully')


if __name__ == "__main__":
    main()