/**
 * Module to manage cross-move into i18n sites.
 */
import Cookies from "js-cookie";
import * as packageJson from "../../package.json";

const COOKIE_SELECTED_LANG = "lang";
const COOKIE_MAX_AGE_DAYS = 400;
const ENTRYPONT_MATCHES = ["", "/", "index.html", "/index.html"];

/**
 * Redirect page of selected language.
 */
const redirectWithRemember = (lang: string, url: string) => {
  Cookies.set(COOKIE_SELECTED_LANG, lang, {
    sameSite: "strict",
    path: "/",
    expires: new Date(
      new Date().getTime() + 1000 * 60 * 60 * 24 * COOKIE_MAX_AGE_DAYS,
    ),
  });
  location.href = url;
};

/**
 * Handlers for HTML
 */
export namespace Widget {
  export const redirectLanguageSite = (
    basePath: string,
    defaultLang: string,
  ) => {
    const url = new URL(window.location.href);
    const patterns = ENTRYPONT_MATCHES.map((m) => `${basePath}${m}`);
    if (!patterns.includes(url.pathname)) {
      console.warn("This page is not target for redirection");
      return;
    }
    const targetLang = Cookies.get(COOKIE_SELECTED_LANG) || defaultLang;
    // NOTE:  This is better (keep implement for compatibility and tests).
    // redirectWithRemember(targetLang, `${basePath}${targetLang}/`);
    location.href = `${basePath}${targetLang}/`;
  };

  /**
   * Handler for changing value of selectbox.
   */
  export const redirectBySelect = (e: Event) => {
    if (!(e.target instanceof HTMLSelectElement)) {
      console.error("This handler should be called only from <select>");
      return;
    }
    const langCode = e.target.value;
    const langUrl = e.target.selectedOptions[0].dataset.url ?? false;
    if (langCode && langUrl) {
      redirectWithRemember(langCode, langUrl);
    }
    console.error("Target URL is not found.");
  };
}

console.debug(`Current version is ${packageJson.version}`);
