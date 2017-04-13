{
	"name": "Academic Information System Day",
	"version": "1.0",
	"depends": [
		"base",
		"board",

	],
	"author": "chaerulrifatpauji@gmail.com",
	"category": "Education",
	'website': 'http://www.vitraining.com',
	"description": """\
	Academic Information System Day1
	""",
	"data": [
	"menu.xml",
	"course.xml",
	"session.xml",
	"attendee.xml" ,
	"partner.xml" ,
	"workflow.xml" ,
	"security/group.xml",
	"security/ir.model.access.csv",
	"wizard/create_attendee_view.xml",
	"dashboard.xml",
	"report/session.xml",
	],
	"installable": True,
	"auto_install": False,
	"application": True,
}