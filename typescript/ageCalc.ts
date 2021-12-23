const birthDate: CalendarDate = { year: 1990, month: 'apr', day: 1 };

const today = {
    year: new Date().getFullYear(),
    month: monthName(new Date().getMonth() + 1),
    day: new Date().getDate(),
};

const daysOld = numberOfDaysBetween({ start: birthDate, end: today });
