Name:		texlive-docsurvey
Version:	70729
Release:	1
Summary:	A survey of LaTeX documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/docsurvey
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docsurvey.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docsurvey.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A survey of programming-related documentation for LaTeX.
Included are references to printed and electronic books and
manuals, symbol lists, FAQs, the LaTeX source code, CTAN and
distributions, programming-related packages, users groups and
online communities, and information on creating packages and
documentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/docsurvey

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
