import dayjs from "dayjs";
import 'dayjs/locale/ru'
import {times, identity} from 'ramda';

export function generator() {
    const lanes = [];
    const items = [1, 2, 3];
    lanes.push({
        id: 0,
        title: `все`,
        "style": {"width": 200, backgroundColor: '#db2b21'},
        cards: generateCards(10)
    });
    items.forEach(i => {
        const width = 200 * i;
        lanes.push(
            { id: i, title: `количество ${i}`, "style": {"width": width, backgroundColor: '#db2b21'},
                cards: generateCards()
            }
        )
    });
    return { lanes }
}

function generateDay() {
    const min = 1;
    const max = 5;
    const today = dayjs().locale('ru');
    return today.add(min + (Math.random() * (max-min)), 'hour')
        .add(min + (Math.random() * (max-min)), 'day');
}

function generateCards(count) {
    const cards = [];
    const style = { minWidth: '100%', textAlign: 'left' };
   
    const min = 3;
    const max = 7;
    const rand =  min + (Math.round(Math.random()) * (max-min));
    const arrayLength = count || rand;
    
    times(identity, arrayLength).forEach(i => {
        cards.push({
            id: i,
            title: `${1000 * (i + 1)} шт`,
            description: generateDay().format('hh:mm DD-MM-YYYY'),
            style
        })
    });
    
    return cards
    // cards.sort((a, b) => b.description.isBefore(a.description) })
        // .map( i => i.description.format('hh:mm DD-MM-YYYY'))
}