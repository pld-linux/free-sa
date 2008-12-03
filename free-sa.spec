Name:		free-sa
Version:	1.5.0
Release:	0.1
Summary:	Squid report generator per user/ip/name
URL:		http://free-sa.sourceforge.net/
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	247d942cbe5cbb86c7d2fc1616646c4c
Patch0:		%name-global.mk.patch
License:	GPL v3
Group:          Networking

%description
Free-SA is statistic analyzer for daemons log files similar to SARG.
Its main advantages over SARG are much better speed (7x-20x times),
more reports support, crossplatform work and W3C compliance of
generated HTML/CSS reports code.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT/usr

%{__make} -C themes install \
	WWWDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}

install -d $RPM_BUILD_ROOT%{_mandir}
install -d $RPM_BUILD_ROOT%_sysconfdir/%{name}

mv $RPM_BUILD_ROOT/usr/man/* $RPM_BUILD_ROOT/%{_mandir}/
rm -rf $RPM_BUILD_ROOT%{_prefix}/{man,share/doc} 
install etc/free-sa.conf.sample.in $RPM_BUILD_ROOT/%_sysconfdir/%{name}/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog FAQ INSTALL README THANKS
%config(noreplace) %_sysconfdir/%{name}/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_mandir}/man[15]/*
%dir %{_datadir}/%{name}
%dir %_sysconfdir/%{name}
