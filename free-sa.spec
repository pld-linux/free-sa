# TODO: optflags
Summary:	Squid report generator per user/IP/name
Summary(pl.UTF-8):	Generator raportów ze squida
Name:		free-sa
Version:	1.6.0
Release:	0.1
License:	GPL v3
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/free-sa/%{name}-%{version}.tar.gz
# Source0-md5:	e013ef81f53a034528cda62772ab0a21
Patch0:		%{name}-global.mk.patch
URL:		http://free-sa.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free-SA is statistic analyzer for daemons log files similar to SARG.
Its main advantages over SARG are much better speed (7x-20x times),
more reports support, crossplatform work and W3C compliance of
generated HTML/CSS reports code.

%description -l pl.UTF-8
Free-SA jest podobnym do SARG analizatorem statystyk z logów demonów.
Jego główną przewagą nad SARG jest szybkość (7-20 razy większa),
obsługa większej liczby raportów, wieloplatformowość oraz zgodność
wygenerowanego kodu HTML/CSS z wytycznymi W3C.

%prep
%setup -q
#%patch0 -p0

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%{__make} -C themes install \
	WWWDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_mandir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

mv $RPM_BUILD_ROOT%{_prefix}/man/* $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/{man,share/doc}
install etc/free-sa.conf.sample.in $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog FAQ INSTALL README THANKS
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man[15]/*
