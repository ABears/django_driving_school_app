const token = document.querySelector('.get-csrf').childNodes[1].value;

const calendar = new HelloWeek({
    selector: '.hello-week',
    lang: 'en',
    langFolder: '/static/hello-week-master/dist/langs/',
    format: 'dd/mm/yyyy',
    weekShort: true,
    monthShort: false,
    multiplePick: false,
    defaultDate: false,
    todayHighlight: true,
    daysSelected: null,
    disablePastDays: true,
    disabledDaysOfWeek: false,
    disableDates: false,
    weekStart: 0, // 0 (Sunday) to 6 (Saturday).
    daysHighlight: true,
    range: false,
    rtl: false,
    locked: false,
    minDate: false,
    maxDate: false,
    nav: ['◀', '▶'],
    daysHighlight: [
  ],
    onLoad: reloadAppointement,
    onChange: updateInfo,
    onSelect: updateInfo
  //   onClear: updateInfo
    
  });

  const today = document.querySelector('.demo-today');
  const picked = document.querySelector('.demo-picked');
  const last = document.querySelector('.demo-last');

  String.prototype.replaceAll = function(target, replacement) {
    return this.split(target).join(replacement);
  };

  function reloadAppointement(){

    let getAppointementUrl = '/read-general-planning';
    let data = {csrfmiddlewaretoken: token }
    let bookedAppointement = []

    $.ajax({
      type: "POST",
      url: getAppointementUrl,
      data: data,
      success: function(response) {
          
        const allAppointement = response.all_appointement;

        for (let key in allAppointement){

          let appointement = allAppointement[key];
          appointementFormatDate = '';
          appointementFormatDate +=  new Date(appointement.appointement_date).getFullYear() + '-';

          if(Number(new Date(appointement.appointement_date).getMonth()) + 1 < 10){
            appointementFormatDate += '0';
          }

          appointementFormatDate +=  Number(new Date(appointement.appointement_date).getMonth()) + 1;
          appointementFormatDate += '-' + new Date(appointement.appointement_date).getDate();

          bookedAppointement[key] = appointementFormatDate

        }

      }
    }).then(() =>{

      calendar.setDaysHighlight([
        {days: bookedAppointement, backgroundColor: '#f08080'},
      ]);

      calendar.update();  
    })

  }

  function updateInfo() {

      
    if (this.today) {
        today.innerHTML = '';
        var li = document.createElement('li');
        li.innerHTML = this.today;
        today.appendChild(li);
    }

    if (this.lastSelectedDay) {

        last.innerHTML = '';
        var li = document.createElement('h2');
        li.classList.add('get-current-day');
        li.innerHTML += new Date(this.lastSelectedDay).getDate() + '/';
        li.innerHTML += Number(new Date(this.lastSelectedDay).getMonth()) + 1;
        li.innerHTML += '/' + new Date(this.lastSelectedDay).getFullYear();
        last.appendChild(li);

        let fullDate = li.innerHTML

        getDayGeneralPlanning(fullDate.replaceAll('/', '-'));

    }

}


function getDayGeneralPlanning(fullDate){

  let getDayPlanningUrl = '/read-day-general-planning/' + fullDate;
  let getUserBaseUrl = '/read-user/';
  let data = {csrfmiddlewaretoken: token };

    $.ajax({
      type: "POST",
      url: getDayPlanningUrl,
      data: data,
      success: function(response) {

        $('#day-planning').html('');

        const allAppointement = response.all_appointement;

        for (let key in allAppointement){

          let appointement = allAppointement[key];
          let getInstructor = ''
          let getStudent = ''
          $.ajax({
            type: "POST",
            url: getUserBaseUrl + appointement.instructor_id,
            data: data,
            success: function(response) {
              
              getInstructor = response.subject_user[0].last_name + ' ' + response.subject_user[0].first_name;
              
            }
          })
          .then(() => {
            $.ajax({
              type: "POST",
              url: getUserBaseUrl + appointement.student_id,
              data: data,
              success: function(response) {

                getStudent = response.subject_user[0].last_name + ' ' +response.subject_user[0].first_name;

              }
            })
            .then(() => {
              $('#day-planning').append('<div class="row p-5 border"></br><div class="col-md-8 col-sm-8 col-lg-8"> <span class="text-success">' + getInstructor + '</span> / <span class="font-weight-bold">' + getStudent + '</span></div><div class="col-md-4 col-sm-4 col-lg-4 border-left">'+ new Date(appointement.appointement_date).getUTCHours() + ' H </div></div>');
            })
          })

        }

      }
    })
  
}
