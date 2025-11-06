// Filtragem simples de cards por texto ou keywords (busca em todo o conteúdo do card)
(function(){
    const input = document.getElementById('filter');
    const clearBtn = document.getElementById('clear');
    const grid = document.getElementById('menu');
    const cards = Array.from(grid.querySelectorAll('.card'));

    function normalize(s){
        return (s||'').toString()
            .toLowerCase()
            .trim()
            .normalize('NFD')
            .replace(/[\u0300-\u036f]/g, '');
    }

    function filter(q){
        const qn = normalize(q);
        if(!qn){
            cards.forEach(c => c.style.display = 'flex');
            return;
        }
        cards.forEach(card => {
            // concatena todo o texto do card + keywords
            const content = normalize(card.textContent + ' ' + (card.dataset.keywords || ''));
            const match = content.includes(qn)
                || qn.split(/\s+/).every(token => content.includes(token));
            card.style.display = match ? 'flex' : 'none';
        });
    }

    input.addEventListener('input', e => filter(e.target.value));
    if(clearBtn) clearBtn.addEventListener('click', () => { input.value=''; filter(''); input.focus(); });

    // permitir busca via Escape para limpar
    input.addEventListener('keydown', e => {
        if(e.key === 'Escape') { input.value=''; filter(''); }
    });
})();
