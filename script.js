// Filtragem simples de cards por texto ou keywords
(function(){
    const input = document.getElementById('filter');
    const clearBtn = document.getElementById('clear');
    const grid = document.getElementById('menu');
    const cards = Array.from(grid.querySelectorAll('.card'));

    function normalize(s){ return (s||'').toString().toLowerCase().trim(); }

    function filter(q){
        const qn = normalize(q);
        if(!qn){
            cards.forEach(c=> c.style.display='flex');
            return;
        }
        cards.forEach(card=>{
            const title = normalize(card.querySelector('h3')?.textContent);
            const desc = normalize(card.querySelector('p')?.textContent);
            const kw = normalize(card.dataset.keywords);
            const match = title.includes(qn) || desc.includes(qn) || kw.includes(qn) || qn.split(/\s+/).every(token => (title+desc+kw).includes(token));
            card.style.display = match ? 'flex' : 'none';
        });
    }

    input.addEventListener('input', e => filter(e.target.value));
    clearBtn.addEventListener('click', () => { input.value=''; filter(''); input.focus(); });

    // permitir busca via Escape para limpar
    input.addEventListener('keydown', e => {
        if(e.key === 'Escape') { input.value=''; filter(''); }
    });
})();
