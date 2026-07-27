/* НПК Механик — UI behaviour. No dependencies. */
(function () {
  'use strict';

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Mobile navigation ---------- */
  var burger = document.querySelector('[data-burger]');
  var mnav = document.querySelector('[data-mobile-nav]');

  if (burger && mnav) {
    var setNav = function (open) {
      burger.setAttribute('aria-expanded', String(open));
      mnav.dataset.open = String(open);
      document.body.style.overflow = open ? 'hidden' : '';
    };
    burger.addEventListener('click', function () {
      setNav(burger.getAttribute('aria-expanded') !== 'true');
    });
    mnav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && burger.getAttribute('aria-expanded') === 'true') {
        setNav(false);
        burger.focus();
      }
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 860) setNav(false);
    });
  }

  /* ---------- Scroll reveal ---------- */
  var revealables = document.querySelectorAll('[data-reveal]');
  if (reduced || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        var delay = Number(el.dataset.revealDelay || 0);
        setTimeout(function () { el.classList.add('is-in'); }, delay);
        io.unobserve(el);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------- Model filter ---------- */
  var filters = document.querySelectorAll('[data-filter]');
  var models = document.querySelectorAll('[data-kind]');
  var counter = document.querySelector('[data-model-count]');

  if (filters.length && models.length) {
    var apply = function (kind) {
      var shown = 0;
      models.forEach(function (m) {
        var match = kind === 'all' || m.dataset.kind === kind;
        m.hidden = !match;
        if (match) shown++;
      });
      if (counter) counter.textContent = String(shown);
    };
    filters.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filters.forEach(function (b) { b.setAttribute('aria-pressed', String(b === btn)); });
        apply(btn.dataset.filter);
      });
    });
  }

  /* ---------- Request form ---------- */
  var form = document.querySelector('[data-form]');
  if (form) {
    var rules = {
      name: function (v) { return v.trim().length >= 2 || 'Укажите имя'; },
      phone: function (v) {
        var digits = v.replace(/\D/g, '');
        return digits.length >= 10 || 'Телефон должен содержать не менее 10 цифр';
      }
    };

    var showError = function (input, message) {
      var box = input.parentElement.querySelector('.err');
      if (message) {
        input.setAttribute('aria-invalid', 'true');
        if (box) box.textContent = message;
      } else {
        input.removeAttribute('aria-invalid');
        if (box) box.textContent = '';
      }
    };

    var validate = function (input) {
      var rule = rules[input.name];
      if (!rule) return true;
      var result = rule(input.value);
      showError(input, result === true ? '' : result);
      return result === true;
    };

    form.querySelectorAll('input, textarea').forEach(function (input) {
      input.addEventListener('blur', function () { validate(input); });
      input.addEventListener('input', function () {
        if (input.getAttribute('aria-invalid') === 'true') validate(input);
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fields = Array.prototype.slice.call(form.querySelectorAll('input[name], textarea[name]'));
      var invalid = fields.filter(function (f) { return !validate(f); });

      if (invalid.length) {
        invalid[0].focus();
        return;
      }

      var button = form.querySelector('button[type="submit"]');
      if (button) { button.disabled = true; button.textContent = 'Отправляем…'; }

      // Точка интеграции: замените на реальный endpoint (CRM / почта / Telegram bot).
      setTimeout(function () {
        var ok = document.createElement('p');
        ok.className = 'form__ok';
        ok.setAttribute('role', 'status');
        ok.textContent = 'Заявка принята. Инженер свяжется с вами в течение рабочего дня.';
        form.replaceChildren(ok);
      }, 600);
    });
  }

  /* ---------- Phone mask (light touch) ---------- */
  var phone = document.querySelector('input[name="phone"]');
  if (phone) {
    phone.addEventListener('input', function () {
      var d = phone.value.replace(/\D/g, '').slice(0, 11);
      if (!d) { phone.value = ''; return; }
      if (d[0] === '8') d = '7' + d.slice(1);
      var out = '+' + d[0];
      if (d.length > 1) out += ' (' + d.slice(1, 4);
      if (d.length >= 5) out += ') ' + d.slice(4, 7);
      if (d.length >= 8) out += '-' + d.slice(7, 9);
      if (d.length >= 10) out += '-' + d.slice(9, 11);
      phone.value = out;
    });
  }

  /* ---------- Active section in nav ---------- */
  var sections = document.querySelectorAll('main section[id]');
  var navLinks = document.querySelectorAll('.nav a[href^="#"]');
  if (sections.length && navLinks.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (a) {
          a.toggleAttribute('aria-current', a.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }
})();
