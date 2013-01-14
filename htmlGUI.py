
class htmler:
	sliders = """                <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-1>                        <label for="slider1">                            Value:                        </label>                        <input type="range" name="slider" id="slider-1" value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>                <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-2>                        <label for="slider2">                            Value:                        </label>                        <input type="range" name="slider" id=slider-2 value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>                <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-3>                        <label for="slider3">                            Value:                        </label>                        <input type="range" name="slider" id=slider-3 value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>                <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-4>                        <label for="slider4">                            Value:                        </label>                        <input type="range" name="slider" id=slider-4 value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>                 <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-5>                        <label for="slider5">                            Value:                        </label>                        <input type="range" name="slider" id=slider-5 value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>                <div data-role="fieldcontain">                    <fieldset data-role="controlgroup" id=container-6>                        <label for="slider6">                            Value:                        </label>                        <input type="range" name="slider" id=slider-6 value="50" min="0" max="100" data-highlight="false" />                    </fieldset>                </div>"""
	index_header = """<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset="utf-8" />\n        <meta name="viewport" content="width=device-width, initial-scale=1" />\n        <title>\n        </title>\n        <link rel="stylesheet" href="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.2.0/jquery.mobile-1.2.0.min.css" />\n        <!--<link rel="stylesheet" href="my.css" />-->\n        <style>\n            /* App custom styles */\n        hr.style-eight {\n border: none;\n    border-top: medium double #333;\n    color: #333;\n    text-align: center;\n}\n    </style>\n        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js">\n        </script>\n        <script src="https://ajax.aspnetcdn.com/ajax/jquery.mobile/1.2.0/jquery.mobile-1.2.0.min.js">\n        </script>\n        <!--<script src="my.js">-->\n        </script>\n    </head>\n    <body>\n        <!-- Home -->\n        <div data-role="page" id="page1">\n            <div data-theme="a" data-role="header" style="cursor:pointer;" id="header">\n                <table width=100% cellpadding=0 cellspacing=0 border=0>\n            <tr>\n             <td align=left><img src=http://hangar.org/A2R/img/A2R_logo_trans.png height=55></td>\n             <td align=center width=100%><h3 id="header_title"> Addicted2Random Active Sessions </h3></td>\n                   <td align=right><img src=http://hangar.org/A2R/img/A2R_arrow_trans.png height=55></td>\n                </tr>\n         </table>\n            </div>\n<div id=player align=center><audio id=audio_player controls><source id=ogg_src src=""  type="audio/ogg"></audio></div>            <div data-role="content" align=center id="content">\n"""
	index_footer = """            </div>\n            <div data-theme="a" data-role="footer" data-position="fixed" align=center>\n                <a href="http://blog.radiofabrik.at/a2r/" target=_blank>\n                    Addicted2Random blog\n                </a>\n            </div>\n        </div>\n        <script>\nvar header_title_text="Addicted2Random Active Sessions";\n var session_title_text="";\nvar proxy_address="";\nvar proxy_port=77777;\n            //App custom javascript\n$('div[name^="session"]').click(function() {\n $('#header_title').html('"'+$('span[name=title_'+$(this).attr('name')+']').html()+'" by '+$('span[name=author_'+$(this).attr('name')+']').html());\n$('#session_template').css("display","block"); $('#sessions_list').css("display","none");\nproxy_address = $('span[name=proxy_'+$(this).attr('name')+']').html();\nproxy_port = $('span[name=port_'+$(this).attr('name')+']').html();\nvar audio = $("#audio_player");\n$("#ogg_src").attr("src", $('span[name=stream_'+$(this).attr('name')+']').html());\naudio[0].pause();\naudio[0].load();\naudio[0].play(); \n }); $('div[name^="session"]').mouseover(function() {\n  $('hr[name='+$(this).attr('name')+']').attr("class","style-eight");\n$(this).css("background","white");\n});\n$('div[name^="session"]').mouseout(function() {\n  $(this).css("background","none");\n$('hr[name='+$(this).attr('name')+']').attr("class","none");\n});\n $('#header').click(function() {\n location.reload();\n});\n$('#header').mouseover(function() {\n if ($('#header_title').html() != header_title_text) { session_title_text=$('#header_title').html(); $('#header_title').html(header_title_text);} });\n$('#header').mouseout(function() {\n if (session_title_text!="") $('#header_title').html(session_title_text); }); \n$("#container-1").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "1", val : $("#slider-1").val()}); \n});\n$("#container-2").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "2", val : $("#slider-2").val()}); \n});\n$("#container-3").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "3", val : $("#slider-3").val()}); \n});\n$("#container-4").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "4", val : $("#slider-4").val()}); \n});\n$("#container-5").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "5", val : $("#slider-5").val()}); \n});\n$("#container-6").change(function() { $.get("/send_data", { address : proxy_address, port : proxy_port, sensor : "6", val : $("#slider-6").val()}); \n});\n         </script>\n    </body>\n</html>"""
	def build_index(self,sessions):
		if (len(sessions) > 0):
		    ans = "<p>There are "+str(len(sessions))+" active sessions in this server. Click over a session to start playing.</p>";
		    for session in sessions:
			ans = ans + "<div name=session_"+session['_id']+" style='cursor:pointer'><hr name=session_"+session['_id']+" >\n"
			for val in session:
				if (val!='token')and(val!='__v')and(val!='statistic')and(val!='_id'):
				    ans = ans + "<b>"+val+"</b> <span name="+val+"_session_"+session['_id']+">"+str(session[val])+"</span><br>\n"
			ans = ans + "<hr name=session_"+session['_id']+" ></div><br>\n"
		else:
		    ans = "<br><br><p>Sorry, there are no open sessions for the moment in this server.";		
		
		return self.index_header+"<div id='session_template' style='display:none;'>"+self.sliders+"</div>\n"+"<div id='sessions_list'>"+ans+"</div>"+self.index_footer
	